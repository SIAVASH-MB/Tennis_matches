# Which player has the highest number of wins?
# 
# 
# 
# 
# 
# 
# 
# 
# 
#  
import pandas as pd
pd.set_option('display.max_columns', None)  # Show all columns
A=pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchEventInfo.csv")


#Winnings=Matches[["match_id","winnig"]][Matches["winnig"]==True]
print(A.head(20))