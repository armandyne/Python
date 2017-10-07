i=input("Type 1 for actual, or nothing for sample data: ") 
if i is None or i != "1": 
    filename = "regex_sum_42.txt"
else:
    filename = "regex_sum_37776.txt"

directory = "Using Python to Access Web Data/Extracting Data With Regular Expressions/data"    
    
try:
    f = open(directory+"/"+filename)
except:
    print("Cant open text file")

lines = f.read()
#print(lines)

import re

numbers = re.findall('[0-9]+', lines)
#print(numbers)

sumOfNumbers = 0
for x in numbers:
    sumOfNumbers = sumOfNumbers + int(x)

print(sumOfNumbers)    
