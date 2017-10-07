import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter initial URL: ")
pos = input("Enter position for next URL: ")
count = input("Enter counts of repetition: ")
pos = int(pos)

names = list()

for i in range(int(count)+1):	
	html = urllib.request.urlopen(url, context=ctx).read()
	print("Retrieving: ", url)
	
	soup = BeautifulSoup(html, "html.parser")
	tags = soup("a")

	if i != int(count):
		names = names + [tags[pos-1].getText()]
		url = tags[pos-1].get("href", None)

print(names)	
