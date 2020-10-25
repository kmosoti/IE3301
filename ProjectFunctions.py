from math import ceil
def fileToList(data):
    tempList = [float(line.rstrip()) for line in open(data)]
    tempList.sort()
    return tempList
def findAverageFile(data):
    #dataFile = open(data,"r")
    tempList = [line.rstrip() for line in open(data)]
    for index, item in enumerate(tempList):
        tempList[index] = float(item)
    #Grabs sum
    sum = 0
    for num in tempList:
        sum += num
    #Gets average and returns
    average = sum/len(tempList)
    return average

def findSTDDEVFile(data,mean):
    tempList = [line.rstrip() for line in open(data)]
    for index, item in enumerate(tempList):
        tempList[index] = float(item)
    
    #grabs numerator of function
    numerator = list(map(
                        lambda i: round((i-mean)**2,4), tempList
                        )
                    )
    
    numSum = 0
    for num in tempList:
        numSum += num
    
    stddev = (numSum/(len(tempList)-1))**0.5
    return stddev

def findQuartilesFile(data):
    tempList = [line.rstrip() for line in open(data)]
    for index, item in enumerate(tempList):
        tempList[index] = float(item)
    
    tempList.sort()
    Q1 = tempList[ceil((0.25 * len(tempList))-1)]
    Q2 = tempList[ceil((0.5 * len(tempList))-1)]
    Q3 = tempList[ceil((0.75 * len(tempList))-1)]

    Quartiles = [Q1,Q2,Q3]
    return Quartiles
    
    tempList.sort()
