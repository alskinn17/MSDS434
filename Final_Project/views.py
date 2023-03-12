from flask import Blueprint, render_template, request, jsonify, redirect, url_for


views = Blueprint(__name__, "views")

@views.route("/", methods=['GET'])
def home():
    teams = ['Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford',
             'Brighton & Hove Albion', 'Chelsea', 'Crystal Palace',
             'Everton', 'Fulham', 'Leeds United', 'Leicester City',
             'Liverpool', 'Manchester City', 'Manchester United',
             'Newcastle United', 'Nottingham Forest', 'Southampton',
             'Tottenham Hotspur', 'West Ham United', 'Wolverhampton Wanderers']
    return render_template("index.html", teams=teams)

#this will be used to show each teams stats in a table
# @views.route("/<team>")
# def team_stats(team):
#     args = requests.args
#     name = args.get('team')
#     return render_template()

@views.route("/test", methods=['POST', 'GET'])
def test():
    teams = ['Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford',
             'Brighton & Hove Albion', 'Chelsea', 'Crystal Palace',
             'Everton', 'Fulham', 'Leeds United', 'Leicester City',
             'Liverpool', 'Manchester City', 'Manchester United',
             'Newcastle United', 'Nottingham Forest', 'Southampton',
             'Tottenham Hotspur', 'West Ham United', 'Wolverhampton Wanderers']
    hometeam = request.form.get('hometeam')
    awayteam = request.form.get('awayteam')
    return render_template("index2.html", teams=teams)    



@views.route("/json")
def get_json():
    return jsonify({'name': 'alex', 'age': '29'})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))

