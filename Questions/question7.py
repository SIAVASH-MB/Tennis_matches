#  What is the average number of aces per match?
import pandas as pd
pd.set_option('display.max_columns', None)  # Show all columns
PeriodInfo= pd.read_csv("Tennis_matches/Dataset/PeriodInfo.csv",usecols=["match_id", "statistic_name"])
Match_count=PeriodInfo["match_id"].nunique()  # Count unique matches
Ace_count = PeriodInfo["statistic_name"].str.contains("ace", case=False, na=False).sum()  # Count aces
Average_aces_per_match = Ace_count / Match_count if Match_count > 0 else 0  # Calculate average
print(f"Average number of aces per match: {Average_aces_per_match}")