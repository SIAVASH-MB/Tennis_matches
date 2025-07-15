# 10. Is there a correlation between a player's height and their ranking? 
import pandas as pd
import numpy as np
Away_Team = pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchAwayTeamInfo.csv")
Home_Team = pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchHomeTeamInfo.csv")
DF_Away=Away_Team[["match_id", "name", "current_rank", "height"]]
DF_Home=Home_Team[["match_id", "name", "current_rank", "height"]]
DF = pd.concat([DF_Away, DF_Home], ignore_index=True)
DF = DF.rename(columns={"name": "name", "current_rank": "current_rank", "height": "height"})
DF = DF.drop_duplicates(subset=["match_id", "name"])  # Remove duplicates based on match_id and name
DF = DF.reset_index(drop=True)  # Reset index after dropping duplicates
DF = DF[DF["current_rank"].notna() & DF["height"].notna()]  # Filter out rows with NaN values in current_rank or height
correlation = DF["current_rank"].corr(DF["height"])
print(f"Correlation between player's height and their ranking: {correlation}")









