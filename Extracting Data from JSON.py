#Extracting Data from JSON by Mitul
import json
import urllib.request
count = 0

url = input("Give  Actual Data or Website Link")
print ("retrieving URL. Stand by.")
uh = urllib.request.urlopen(url)
data= uh.read()

info = json.loads(data)
for item in info["comments"]:
	#print item["count"]
	number = int(item["count"])
	count = count + number
print( count)


'''Output;
Give  Actual Data or Website Link>? http://py4e-data.dr-chuck.net/comments_450130.json
retrieving URL. Stand by.
2870'''
