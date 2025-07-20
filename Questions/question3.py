# Which player has the highest number of wins?
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)  # Show all columns
PeriodInfo= pd.read_csv("/workspaces/Tennis_matches/Dataset/PeriodInfo.csv",usecols=["match_id", "statistic_name"])
Home_Team=pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchHomeTeamInfo.csv",usecols=["match_id", "name"])
Away_Team=pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchAwayTeamInfo.csv",usecols=["match_id", "name"])
Players= pd.concat([Home_Team, Away_Team], axis=0)
Df = pd.merge(Players, PeriodInfo, on="match_id", how="left")
Df= Df[Df['statistic_name']== 'total_won']
Df = Df.groupby(['name'])["statistic_name"].count().reset_index()
Df = Df.rename(columns={"statistic_name": "sum_won"})
Df = Df.sort_values(by=['sum_won'], ascending=False)
Most_won_player = Df.head(1)
print(Most_won_player)
