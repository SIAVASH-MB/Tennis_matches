# 9. Which player has won the most tournaments in a single month?
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)  # Show all columns
#tounaments = pd.read_csv('/workspaces/Tennis_matches/Dataset/MatchTournamentInfo.csv',usecols=["match_id", "tournament_name"])
PeriodInfo= pd.read_csv("Tennis_matches/Dataset/PeriodInfo.csv",usecols=["match_id", "statistic_name"])
Home_Team=pd.read_csv("Tennis_matches/Dataset/MatchHomeTeamInfo.csv",usecols=["match_id", "name"])
Away_Team=pd.read_csv("Tennis_matches/Dataset/MatchAwayTeamInfo.csv",usecols=["match_id", "name"])
date = pd.read_csv('Tennis_matches/Dataset/MatchEventInfo.csv', usecols=["match_id", "start_datetime"])
date['start_datetime'] = pd.to_datetime(date['start_datetime'], unit='s')
date['month'] = date['start_datetime'].dt.month
date['month_name'] = date['start_datetime'].dt.strftime('%B')
Players= pd.concat([Home_Team, Away_Team], axis=0)
#Df = pd.merge(tounaments, Players, on="match_id", how="left", suffixes=('', '_player'))
Df = pd.merge(Players, PeriodInfo, on="match_id", how="left")
Df = pd.merge(Df, date, on="match_id", how="left")
Df= Df[Df['statistic_name']== 'total_won']
Df = Df.groupby(['name', 'month_name'])["statistic_name"].count().reset_index()
Df = Df.rename(columns={"statistic_name": "sum_won"})
Df = Df.sort_values(by=['month_name', 'sum_won'], ascending=False)
Df = Df.groupby('month_name').head(1).reset_index(drop=True)
Most_won = Df.sort_values(by='sum_won', ascending=False).head(1)
print(Most_won)