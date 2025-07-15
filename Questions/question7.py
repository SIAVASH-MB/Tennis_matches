#  What is the average number of aces per match?











import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)  # Show all columns
A= pd.read_csv("/workspaces/Tennis_matches/Dataset/OddsInfo.csv")  # or the correct file
print(A.columns)  # See available columns   
print(A.head(5))  # Display the first few rows to understand the structure