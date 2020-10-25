from ProjectFunctions import findAverageFile,findSTDDEVFile,findQuartilesFile,fileToList


#Will contain print functions for Averages, Standard Deviation, Quartiles
print("-----------------------------------")
file = "BlackBerries.txt"
BBaverage = findAverageFile(file)
BBstdev = findSTDDEVFile(file,BBaverage)
BBQuartiles = findQuartilesFile(file)
print("\n-----FINDINGS FROM %s----- \nAverage = %f \nStandard Deviation = %f" %(file,BBaverage,BBstdev))
print("\nQuartiles:\n Q1 = %d \n Q2 = %d \n Q3 = %d" %(BBQuartiles[0],BBQuartiles[1],BBQuartiles[2]))

file2 = "McDonaldsDriveThru.txt"
MCaverage = findAverageFile(file2)
MCstdev = findSTDDEVFile(file2,MCaverage)
MCQuartiles = findQuartilesFile(file2)
print("\n-----FINDINGS FROM %s----- \nAverage = %f \nStandard Deviation = %f" %(file2,MCaverage,MCstdev))
print("\nQuartiles:\n Q1 = %d \n Q2 = %d \n Q3 = %d" %(MCQuartiles[0],MCQuartiles[1],MCQuartiles[2]))
print("-----------------------------------\n")

