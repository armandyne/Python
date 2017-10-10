import sqlite3
import re

data = open("mbox.txt").read()
orgs = re.findall("From: \S+@(\S+)", data)
#print(data)
#print(orgs)

orgscount = dict()
for x in orgs:
    orgscount[x] = orgscount.get(x,0)+1

print(orgscount)

db = sqlite3.connect("emaildb.sqlite")
cur = db.cursor()

for k,v in orgscount.items():
    cur.execute('''INSERT INTO Counts(org, count)
                VALUES (?, ?)''', (k,v))

db.commit() 

for r in cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'):
    print(str(r[0]),str(r[1]))
    
cur.close()

