#Scraping Numbers from HTML using BeautifulSoup by Mitul
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
lst = list()
sum = 0

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
for tag in tags:
    strtag = str(tag)
    lst = re.findall('[0-9+]+',strtag)
    sum = sum + int(lst[0])
print(sum)


'''Output:
Enter - http://py4e-data.dr-chuck.net/comments_450127.html
2539'''
