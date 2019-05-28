import os
import pandas

df1=pandas.read_csv("supermarkets.csv")

print(df1)
print(len(df1.loc[0,::]))

# for i in list(range(0,len(df1))):
# 	print(df1.loc[i,::])

