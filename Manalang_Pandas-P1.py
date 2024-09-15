# Problem#1: Saving a file 
#access pandas features 
import pandas as pd

#Get the data of the provided file which is cars.csv
df = pd.read_csv("cars.csv")

#set variables for the two rows
r = df.iloc[0:5]
q = df.iloc[27:32]

#tries to concatenates the two rows
row = pd.concat([r,q])
print (row)