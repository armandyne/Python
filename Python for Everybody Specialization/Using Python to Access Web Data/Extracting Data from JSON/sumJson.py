import urllib.request
import json

# sample http://py4e-data.dr-chuck.net/comments_42.json
url = input('Enter location: ')
if url is None or len(url)<1:
    print('Empty URL')
else:
    print('Retrieving',url) 
    js = json.loads(urllib.request.urlopen(url).read().decode())
    print('Count:',len(js['comments']))
    
    datasum = 0
    for i in js['comments']:
        #print(i['count'])
        datasum = datasum + int(i['count'])
    print('Sum:',datasum)
