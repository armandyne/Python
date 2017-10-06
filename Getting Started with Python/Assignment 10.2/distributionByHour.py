name = input("Enter file:")
if len(name) < 1 : name = "data/mbox-short.txt"
handle = open(name)

hoursDict = dict()
for line in handle:
    if line.startswith("From "):
        h=line.split()[5].split(":")[0]
        hoursDict[h]=hoursDict.get(h,0)+1
        
#print(hoursDict)        
hoursList = list()
for (k,v) in hoursDict.items():
    hoursList.append((k,v))

hoursList = sorted(hoursList)  
#print(hoursList)

for t in hoursList:
    print(t[0], t[1])