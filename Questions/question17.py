
import pandas as pd
import csv


InfoFile = pd.read_csv('MatchEventInfo.csv')

df = pd.DataFrame(InfoFile)
#
BOS = df[['first_to_serve','winner_code']].dropna()
FirstToServe =BOS['first_to_serve'].to_list()
WinnerCode = BOS['winner_code'].to_list()


num1 = 0
num2 = 22353

for i in range(0,22353):
    if FirstToServe[i] != WinnerCode[i]:
        num1 += 1
    else:
        num1 = num1


result = (num1 / num2) *100  


print(result)