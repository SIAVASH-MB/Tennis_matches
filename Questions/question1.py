#  1. How many tennis players are included in the dataset? 

import pandas as pd
import numpy as np
Away_team=pd.read_csv("MatchAwayTeamInfo.csv")
Inhome_team=pd.read_csv("MatchHomeTeamInfo.csv")
All_Players=pd.concat([Away_team["player_id"],Inhome_team["player_id"]],axis=0)
print("The number of tennis players in the dataset is: ", len(All_Players.unique()))