# 14. What is the most common type of surface used in tournaments? 
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)  # Show all columns
Match_info= pd.read_csv("MatchTournamentInfo.csv")
Ground_type=Match_info["ground_type"].value_counts()
Ground_type.name = "Count"
Ground_type = Ground_type.reset_index()
Ground_type.columns = ["Ground_type", "Count"]
#Ground_type.rename(columns={"Ground_type":"Ground_type","count":"Count"})
Ground_type["Percentage"]=round(Ground_type["Count"]/(Ground_type["Count"].sum())*100,2)
print(f"the most common type of surface used in tournaments is",Ground_type["Ground_type"][1])