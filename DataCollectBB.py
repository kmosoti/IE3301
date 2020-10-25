import random

dataFile = open("McDonaldsDriveThru.txt","w")
for x in range(100):
    dataFile.write(str(round(random.uniform(100, 500),2)) +"\n")
dataFile.close()
