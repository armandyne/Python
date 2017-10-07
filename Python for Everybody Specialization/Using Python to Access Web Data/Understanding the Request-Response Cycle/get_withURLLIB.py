import urllib.request as req
f=req.urlopen("http://data.pr4e.org/intro-short.txt")
print(f.read().decode())