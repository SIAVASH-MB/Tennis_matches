import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)  # Show all columns
Match_info= pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchTournamentInfo.csv")
Ground_type=Match_info["ground_type"].value_counts()
print(Ground_type.head(10))  # Print first 5 rows to check the data