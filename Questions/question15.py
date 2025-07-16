# 15. How many distinct countries are represented in the dataset? 
import pandas as pd
C_Venue=pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchVenueInfo.csv",usecols=["country"])
C_M_Away=pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchAwayTeamInfo.csv",usecols=["country"])
C_M_Home=pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchHomeTeamInfo.csv",usecols=["country"])
Unified_DF=pd.concat([C_M_Away["country"],C_M_Home["country"],C_Venue["country"]],axis=0)
Final_list=Unified_DF.nunique()
print(f"Number of distinct countries which are represented in the dataset is:",Final_list)















