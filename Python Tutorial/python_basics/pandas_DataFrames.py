import pandas

df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]]) # DataFrame creates a data table
print(df1)

#result of print(df1)
"""
     0  1  2 
  0  2  4  6      --> rows have indices and columns have names
  1 10 20 30
"""

df2 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns = ["Price", "Age", "Value"]) # naming the columns
print(df2)

#result of print(df2)
'''
   Price  Age  Value
0      2    4      6
1     10   20     30
'''

df3 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns = ["Price", "Age", "Value"], index = ["First", "Second"]) # naming the rows
print(df3)

#result of print(df3)
'''
        Price  Age  Value
First       2    4      6
Second     10   20     30
'''

df4 = pandas.DataFrame([{"Name": "Amay"}, {"Name": "Joe"}]) # another way of creating DataFrames with dictionaries
print(df4)

# result of print(df4)
'''
   Name
0  Amay
1   Joe
'''

df5 = pandas.DataFrame([{"Name": "Amay", "Surname": "Jain"}, {"Name": "Joe"}]) # adding another column
print(df5)

# result of print(df5)
'''
   Name Surname
0  Amay    Jain
1   Joe     NaN
'''









# Data analysis

df3.mean() # mean of each column
#result
'''
Price     6.0
Age      12.0
Value    18.0
dtype: float64
'''

df3.mean().mean() # mean of entire DataFrame
#result
'''
12.0
'''







#Access a column --> turns DataFrame into a Series
df3.Price
#result
'''
First      2
Second    10
Name: Price, dtype: int64
'''

df3.Price.max() #applying another method to a series
#result
'''
10

