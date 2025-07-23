import pandas as pd 
import numpy as np


ATeam = pd.read_csv('MatchAwayTeamInfo.csv')
HTeam = pd.read_csv('MatchHomeTeamInfo.csv')

dfATeam = pd.DataFrame(ATeam)
dfHTeam = pd.DataFrame(HTeam)

#Top ten players
#---------------------------------------------------------------------
aTeamRank = dfATeam[['player_id','current_rank']].dropna().sort_values(by=['current_rank']).drop_duplicates().head(33)
hTeamRank = dfHTeam[['player_id','current_rank']].dropna().sort_values(by=['current_rank']).drop_duplicates().head(37)

frames1 = [aTeamRank,hTeamRank]
topTenPlayers = pd.concat(frames1).sort_values(by=['current_rank'])

#print(topTenPlayers)
#----------------------------------------------------------------------

#match_ids
#----------------------------------------------------------------------
match_idsAway = dfATeam[['player_id','match_id']]
match_idsHome = dfHTeam[['player_id','match_id']]

frames2 = [match_idsAway,match_idsHome]
match_ids = pd.concat(frames2)


#print(match_ids)
#---------------------------------------------------------------------

#comparing player_ids with match_id for finding the games witch top ten has played
#---------------------------------------------------------------------

def get_matching_values(df1,df2,compare_column,return_colmn):
    matched_df = df2[df2[compare_column].isin(df1[compare_column])]
    return matched_df[return_colmn]


matched_ids = get_matching_values(topTenPlayers,match_ids,'player_id','match_id' )
#print(matched_ids)
#---------------------------------------------------------------------

#
#---------------------------------------------------------------------




print()
#----------------------------------------------------------------------