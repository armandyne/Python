import urllib.request, urllib.parse, urllib.error
import BeautyfulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_37778.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

sumValue = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    sumValue = sumValue + int(tag.getText())
    
print(sumValue)
