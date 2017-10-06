name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emails = dict()

for line in handle:
    if line.startswith("From:"):
        personEmail = line.split()[1]
        emails[personEmail] = emails.get(personEmail,0)+1

greaterKey = None
greaterCount = 0

for k,v in emails.items():
    if greaterKey is None or v>greaterCount:
        greaterKey=k
        greaterCount=v
    
print(greaterKey, greaterCount)        