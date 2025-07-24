# 12. What is the average number of games per set in men's matches compared to women's matches? 
import pandas as pd
import numpy as np
Away_Team = pd.read_csv("Tennis_matches/Dataset/MatchAwayTeamInfo.csv")
Home_Team = pd.read_csv("Tennis_matches/Dataset/MatchHomeTeamInfo.csv")
DF_Away = Away_Team[["match_id", "gender"]]
Df_Home = Home_Team[["match_id","gender"]]
DF = pd.concat([DF_Away, Df_Home], ignore_index=True)
DF = DF.rename(columns={"match_id": "match_id","gender":"gender"})
DF_Players = DF.drop_duplicates(subset=["match_id"])  # Remove duplicates based on match_id
DF_Players = DF_Players.reset_index(drop=True)  # Reset index after dropping duplicates

time= pd.read_csv("Tennis_matches/Dataset/MatchTimeInfo.csv")
time = time[["match_id", "period_1", "period_2", "period_3", "period_4", "period_5"]]
DF_Full = pd.merge(DF_Players, time, on="match_id", how="inner")
#time_per_period = pd.pivot_table(DF_Full, columns="gender",index=["period_1", "period_2", "period_3", "period_4", "period_5"], aggfunc=np.sum)
time_per_period =DF_Full.groupby("gender")[["period_1", "period_2", "period_3", "period_4", "period_5"]].mean().reset_index()
print(time_per_period)







