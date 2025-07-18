# 8. Is there a difference in the number of double faults based on gender? 
import pandas as pd
pd.set_option('display.max_columns', None)  # Show all columns
PeriodInfo= pd.read_csv("/workspaces/Tennis_matches/Dataset/PeriodInfo.csv",usecols=["match_id", "statistic_name"])
PeriodInfo = PeriodInfo[PeriodInfo["statistic_name"].str.contains("double_faults", case=False, na=False)]  # Filter for double faults

Gender_Away=pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchAwayTeamInfo.csv", usecols=["match_id","gender"])
Gender_Home=pd.read_csv("/workspaces/Tennis_matches/Dataset/MatchHomeTeamInfo.csv", usecols=["match_id","gender"])
DB = PeriodInfo.merge(Gender_Away, on="match_id", how="left",suffixes=("", '_away'))
DB = DB.merge(Gender_Home,on="match_id", how="left", suffixes=("", '_home'))
DB = DB.drop_duplicates(subset=["match_id", "statistic_name"])
DB['gender'] = DB['gender'].fillna(DB['gender_home'])
DB["gender_home"] = DB["gender_home"].fillna(DB["gender"])
DB= DB.dropna()
DB.drop(columns=["gender_home"], inplace=True)  # Drop
result=DB.groupby("gender")["statistic_name"].count().reset_index(name="double_faults_count")  # Count double faults by
print(result)  # Print first 100 rows to check the data
