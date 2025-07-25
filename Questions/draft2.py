import pandas as pd

# Load necessary columns
PeriodInfo = pd.read_csv("/workspaces/Tennis_matches/Dataset/PeriodInfo.csv", 
                         usecols=["match_id", "statistic_name", "home_value", "away_value"])

# Filter only rows where statistic is 'aces'
df_aces = PeriodInfo[PeriodInfo['statistic_name'].str.lower() == 'aces']

# Sum aces per match (home + away)
df_aces['total_aces'] = df_aces['home_value'] + df_aces['away_value']

# Group by match and sum total aces
aces_per_match = df_aces.groupby('match_id')['total_aces'].sum()

# Calculate average
average_aces_per_match = aces_per_match.mean()

# Print result
print(f"Average number of aces per match: {average_aces_per_match:.2f}")
