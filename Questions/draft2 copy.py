import pandas as pd
PeriodInfo = pd.read_csv("/workspaces/Tennis_matches/Dataset/PeriodInfo.csv", 
                         usecols=["match_id", "statistic_name", "home_value", "away_value"])
df_aces = PeriodInfo[PeriodInfo['statistic_name'].str.lower() == 'aces']
df_aces['total_aces'] = df_aces['home_value'] + df_aces['away_value']
aces_per_match = df_aces.groupby('match_id')['total_aces'].sum()
average_aces_per_match = aces_per_match.mean()
print(f"Average number of aces per match: {average_aces_per_match:.2f}")
