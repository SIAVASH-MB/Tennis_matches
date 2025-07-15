# Which country has produced the most successful tennis players?
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)  # Show all columns
Events=pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchEventInfo.csv")
Events = Events[["match_id", "winner_code"]] # Select relevant columns
Home_Team=pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchHomeTeamInfo.csv")
Home_Team = Home_Team[["match_id", "name", "country"]]  # Select relevant columns
Away_Team=pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchAwayTeamInfo.csv")
Away_Team = Away_Team[["match_id", "name", "country"]]
DF = pd.merge(Events, Home_Team, on="match_id", how="left", suffixes=('', '_home'))
DF_full = pd.merge(DF, Away_Team, on="match_id", how="left", suffixes=('', '_away'))
DF_full = pd.DataFrame(DF_full)
DF_full["winner_name"] = np.where(DF_full["winner_code"] == 1, DF_full["name"], DF_full["name_away"])
DF_full["winner_country"] = np.where(DF_full["winner_code"] == 1, DF_full["country"], DF_full["country_away"])
DF_winner = DF_full[["winner_name", "winner_country"]]
country_counts = DF_winner["winner_country"].value_counts()
top_countries = country_counts.head(10)
print("Top 3 countries with the most successful tennis players:", top_countries.index.tolist()[:3])
