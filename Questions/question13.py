# 13. What is the distribution of left-handed versus right-handed players? 
# 13. What is the distribution of left-handed versus right-handed players? 
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)  # Show all columns
DF_Away= pd.read_csv("MatchAwayTeamInfo.csv")
DF_Home=pd.read_csv("MatchHomeTeamInfo.csv")
DF_Hand_Home=DF_Home["plays"]
DF_Hand_Away=DF_Away["plays"]
DF_Hand=pd.concat([DF_Hand_Home, DF_Hand_Away], axis=0)
Counts=DF_Hand.value_counts()
Counts = Counts.reset_index()
Counts.columns = ["players_hand", "count"]
Counts["percentage"] = (Counts["count"] / Counts["count"].sum()) * 100
Counts = Counts.sort_values(by="players_hand")
Counts = Counts.reset_index(drop=True)
Counts.plot(kind='bar', x='players_hand', y='percentage', title='Distribution of Left-Handed vs Right-Handed Players')
print(Counts)