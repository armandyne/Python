import urllib.request
import xml.etree.ElementTree as et

url = input('Enter location: ')
if url is None or len(url)==0: 
	print('Empty URL')
else:
	print('Retrieving', url)
	data = urllib.request.urlopen(url).read()
	print('Retrieved', len(data) ,'characters')
	
	xml = et.fromstring(data)
	countsElements = xml.findall('.//count')
	print('Count:',len(countsElements))	
	
	sumCounts = 0
	for e in countsElements:
		sumCounts = sumCounts + int(e.text)
	
	print('Sum:',sumCounts)
