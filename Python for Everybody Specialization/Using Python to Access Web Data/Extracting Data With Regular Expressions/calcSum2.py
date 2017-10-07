import re
file = "Using Python to Access Web Data/Extracting Data With Regular Expressions/data/regex_sum_37776.txt"
print(sum([int(x) for x in re.findall('[0-9]+',open(file).read())]))