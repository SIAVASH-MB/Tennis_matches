# What is the longest match recorded in terms of duration? 
import pandas as pd
pd.set_option('display.max_columns', None)  # Show all columns
DF=pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchTimeInfo.csv")

Durations = DF.groupby("match_id")[["period_1", "period_2", "period_3", "period_4", "period_5"]].sum()
Durations["total_duration"] = Durations.sum(axis=1)
Durations = Durations.reset_index().sort_values(by="total_duration", ascending=False)
print(Durations[["match_id", "total_duration"]].head(1))
