# use bash terminal
# type in --> jupyter notebook

import pandas


df1 = pandas.read_csv("file:///Users/amayjain/Desktop/original/supermarkets.csv")
print(df1)

df2 = pandas.read_json("file:///Users/amayjain/Desktop/original/supermarkets.json")
print(df2)