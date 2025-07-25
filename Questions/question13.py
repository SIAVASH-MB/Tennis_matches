# 13. What is the distribution of left-handed versus right-handed players? 
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)  # Show all columns
DF_Hand_Away= pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchAwayTeamInfo.csv", usecols=["plays", "player_id"])
DF_Hand_Home=pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchHomeTeamInfo.csv", usecols=["plays", "player_id"])
DF_Hand=pd.concat([DF_Hand_Home, DF_Hand_Away], axis=0)
DF_Hand=DF_Hand.drop_duplicates(subset='player_id')
DF_Hand=DF_Hand.reset_index(drop=True)
DF_Hand=DF_Hand.groupby("plays").size().reset_index(name='counts')
DF_Hand=DF_Hand.rename(columns={"plays": "players_hand", "counts": "count"})
DF_Hand["percentage"] = (DF_Hand["count"] / DF_Hand["count"].sum()) * 100
DF_Hand=DF_Hand.sort_values(by="players_hand")
DF_Hand=DF_Hand.reset_index(drop=True)
print("Distribution of Left-Handed vs Right-Handed Players:", DF_Hand)   