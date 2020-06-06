#Following Links in Python by Mitul
import urllib.request
from bs4 import BeautifulSoup

url = input('Enter Url: ')
count = int(input("Enter count: "))
position = int(input("Enter position:"))
for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")

    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
        y = tag.text
        t.append(y)

    print(
    s[position - 1])
    print
    (t[position - 1])
    url = s[position - 1]

'''Output:
Enter Url: http://py4e-data.dr-chuck.net/known_by_Louella.html
Enter count: 7
Enter position:18
http://py4e-data.dr-chuck.net/known_by_Manolo.html
http://py4e-data.dr-chuck.net/known_by_Abhy.html
http://py4e-data.dr-chuck.net/known_by_Joanne.html
http://py4e-data.dr-chuck.net/known_by_Marcy.html
http://py4e-data.dr-chuck.net/known_by_Rhys.html
http://py4e-data.dr-chuck.net/known_by_Alexi.html
http://py4e-data.dr-chuck.net/known_by_Della.html'''

