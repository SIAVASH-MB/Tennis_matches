# What is the average height of the players? 
import pandas as pd
Away_team=pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchAwayTeamInfo.csv")
Inhome_team=pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchHomeTeamInfo.csv")
Away_team_height=Away_team["height"].mean()
Inhome_team_height=Inhome_team["height"].mean()
All_Players_height=(Away_team_height + Inhome_team_height) / 2  
print("Average height of the players is: ", All_Players_height)