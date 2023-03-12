import pandas as pd
import json

df = pd.read_csv('last3.csv')

def select_stats(hometeam, awayteam):

    predictdf = pd.DataFrame()
    
    homedf = df.loc[df['Team'] == hometeam]
    homedf = homedf.drop(columns=['Team'])
    
    awaydf = df.loc[df['Team'] == awayteam]
    awaydf = awaydf.drop(columns=['Team'])
    
    homeseries = homedf.squeeze()
    awayseries = awaydf.squeeze()
    
    predict = homeseries - awayseries
    
    tempdf = predict.to_frame()
    
    predictdf = tempdf.T
    
    predictdf = predictdf.rename(columns={'total_goals_per_match': 'total_goals_per_match_diff', 'half_time_goals_per_match': 'half_time_goals_per_match_diff',
         'shots_per_match': 'shots_per_match_diff', 'shots_on_target_per_match': 'shots_on_target_per_match_diff',
         'fouls_per_match': 'fouls_per_match_diff', 'corners_per_match': 'corners_per_match_diff',
         'yellows_per_match': 'yellows_per_match_diff', 'reds_per_match': 'reds_per_match_diff'})
    
    temp = predictdf.to_json(orient='records')
    data = json.loads(temp)
    final = json.dumps(data, indent=4)
    
    
    return final