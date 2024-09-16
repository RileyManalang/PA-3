# Problem#1: Saving a file 
#access pandas features 
import pandas as pd

#Get the data of the provided file which is cars.csv
df = pd.read_csv("cars.csv")

#using .head() will return the first 5 rows of the dataframe
r = df.head()

#using .tail() will return the last 5 rows of the dataframe
q = df.tail()

print (r)
print (q)
