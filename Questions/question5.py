# How many sets are typically played in a tennis match? 
import pandas as pd
DF= pd.read_csv("/workspaces/Tennis_matches/Dataset/PowerInfo.csv")
most_played=DF["set_num"].mode()  # This will give the most common number of sets played
print("Most played sets in a match: ", most_played[0])  # mode returns a Series, take the first element

max_sets = DF["set_num"].max()  # This will give the maximum number of sets played in any match
print("Maximum sets played in a match: ", max_sets)

often_played = DF["set_num"].value_counts().head(10)  # This will give the top 10 most played sets
print("Top 10 most played sets in matches:\n", often_played)