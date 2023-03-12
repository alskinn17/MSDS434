# msds432-final-project

Microservices:
Ready -
Postgres
Requirement2-microservice
Requirement3-microservice
Requirement5-microservice

In Progress/In Consideration - 
Requirement6-microservice
React.js
Flask


Deployment plan:
This portion is still in progress.
My plan will be to have docker containers for the microservices that can be deployed from your local or linked through google cloud.
These will be able to be pulled from this GitHub page.

The way this would be deployed in an actual setting would be through the docker-compose file in the src folder. 
Each microservice would be run within its own Docker container and would pull from the data lake when necessary.
They would be set to run their respective service on launch and then to repeat the service on set increments or when requested by the web page. 
The web page would have a couple options:
  - Pull entire datasets - this would allow for the end user to have all of whichever dataset if they saw fit
  - Request data from each microservice - allow user to pull the data from any individual microservice
  
Requirement 2 is not completely finished. The way to improve upon it would be to extract the week number from the trip start timestamp.
Then you would be able to see which weeks have the most traffic to which zip codes. You could take the top 10 for each week and then see how the COVID cases
reacted the following week. 

Requirement 6 is not finished. The microservice would use the community area or coordinates to determine the zip code that the permit is in. 
The permit type, community area, and coordiates would be pulled from the building permits dataset. Then you would take the zip code, community area, and 
per capita income from the unemployment dataset. 
The microservice would then do the necessary filtering that is stated in the Final Project Requirements.

This project is currently being run locally on Docker rather than through Google Cloud. 
