import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline 

from ProjectFunctions import findAverageFile,findSTDDEVFile,findQuartilesFile,fileToList

#Loading Variables
file = "BlackBerries.txt"
BlackberryData = fileToList(file)
BBaverage = findAverageFile(file)
BBstdev = findSTDDEVFile(file,BBaverage)
BBQuartiles = findQuartilesFile(file)

file2 = "McDonaldsDriveThru.txt"
McData = fileToList(file2)
MCaverage = findAverageFile(file2)
MCstdev = findSTDDEVFile(file2,MCaverage)
MCQuartiles = findQuartilesFile(file2)

df1 = pd.DataFrame({"Weights(g)": BlackberryData})
df2 = pd.DataFrame({"Time at Mcdonalds(s)": McData})

#BoxPlots
#df1.plot(kind='box', title='Weight of Blackberries Distribution')
#df2.plot(kind='box', title='Wait time in Mcdonalds Drive Thru Distribution')

""" BlackBerryCrossTab = pd.crosstab(index=df1["Weights(g)"],columns="Count")
plt.hist(df1)
plt.xlabel("Weight")
plt.ylabel("Frequency") """

McDonaldsCrossTab = pd.crosstab(index=df2["Time at Mcdonalds(s)"],columns="Count")
plt.hist(df2)
plt.xlabel("Wait Time(s)")
plt.ylabel("Frequency")

plt.show()
