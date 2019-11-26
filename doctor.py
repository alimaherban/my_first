import pandas as pd

dataset=pd.read_csv('test1.csv')

x=dataset.iloc[:3001,:]

print (x)