# 11. What is the average duration of matches?
import pandas as pd
DF=pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchTimeInfo.csv")
Durations = DF.groupby("match_id")[["period_1", "period_2", "period_3", "period_4", "period_5"]].sum()
Durations["total_duration"] = Durations.sum(axis=1)
average_duration = Durations["total_duration"].mean()
print(f"Average match duration: {average_duration} seconds")








