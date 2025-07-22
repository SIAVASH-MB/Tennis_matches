
import pandas as pd
import csv


away_team = pd.read_csv('MatchAwayTeamInfo.csv')
home_team = pd.read_csv('MatchHomeTeamInfo.csv')


df1 = pd.DataFrame(away_team)
df2 = pd.DataFrame(home_team)
#All Players Rank ID Away = apria
apria = df1[['player_id','current_rank']]
aprih = df2[['player_id','current_rank']]

all_players = pd.concat([apria,aprih],axis=0).sort_values(by=['current_rank']).dropna()

playerByRank = all_players['player_id'].unique()



print(all_players['current_rank'])