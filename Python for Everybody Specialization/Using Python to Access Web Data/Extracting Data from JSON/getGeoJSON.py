import urllib.request, urllib.parse
import json
import urllib

#  sample = South Federal University
geoserviceUrl = 'http://py4e-data.dr-chuck.net/geojson?'
university = input('Enter location: ')

if university is None or len(university)<1:
    print('Empty input')
else:
    CompleteUrl = geoserviceUrl + urllib.parse.urlencode({'address':university})
    print('Retrieving', CompleteUrl)
    data = urllib.request.urlopen(CompleteUrl).read().decode()
    print('Retrieved', len(data), 'characters')
    
    js = json.loads(data)
    print('Place id', js['results'][0]['place_id'])