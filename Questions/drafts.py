import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)  # Show all columns
#Match_info= pd.read_csv("/workspaces/Tennis_matches/Dataset/PeriodInfo.csv",usecols=["match_id", "statistic_name", "value"])
#score_Home=pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchHomeScoreInfo.csv")
#score_Away=pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchAwayScoreInfo.csv")
tounaments = pd.read_csv('/workspaces/Tennis_matches/Dataset/MatchEventInfo.csv')
#Nui=Match_info["statistic_name"].unique()
#c=Match_info["statistic_name"].value_counts()  # Count unique values
#print(c)  # Print the counts of unique values
#print(Nui)  # Print first 5 rows to check the data

#v=Match_info["statistic_name"][Match_info["statistic_name"].str.contains("ace", case=False, na=False)   ].count()  # Find unique values containing 'ace'
print(tounaments.sample(100))  # Print the unique values containing 'ace'
#print(Match_info.head(100))  # Print all rows to check the data


df['start_datetime'] = pd.to_datetime(df['start_datetime'], unit='s')

# Extract month (as number)
df['month'] = df['start_datetime'].dt.month

# If you want month name instead
df['month_name'] = df['start_datetime'].dt.strftime('%B')