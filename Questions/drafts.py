import pandas as pd
import numpy as np

time= pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchTimeInfo.csv")
time = time[["match_id", "period_1", "period_2", "period_3", "period_4", "period_5"]]
suum= time["period_5"].sum() 
print(suum)  # Print first 5 rows to check the data