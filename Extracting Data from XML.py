#Extracting Data from XML by Mitul
import urllib.request
import xml.etree.ElementTree as ET
tot = 0
url = input("Enter a location: ")
pg = urllib.request.urlopen(url)
data = pg.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
for i in range(0,len(counts)):
 tot += int(counts[i].text)
 print( 'Retrieved: ', len(data), 'characters')
 print ('Sum: ', tot)








#Output:
'''Enter a location: http://py4e-data.dr-chuck.net/comments_450129.xml
Retrieved:  4218 characters
Sum:  98
Retrieved:  4218 characters
Sum:  194
Retrieved:  4218 characters
Sum:  288
Retrieved:  4218 characters
Sum:  382
Retrieved:  4218 characters
Sum:  473
Retrieved:  4218 characters
Sum:  564
Retrieved:  4218 characters
Sum:  652
Retrieved:  4218 characters
Sum:  739
Retrieved:  4218 characters
Sum:  825
Retrieved:  4218 characters
Sum:  911
Retrieved:  4218 characters
Sum:  997
Retrieved:  4218 characters
Sum:  1081
Retrieved:  4218 characters
Sum:  1165
Retrieved:  4218 characters
Sum:  1244
Retrieved:  4218 characters
Sum:  1322
Retrieved:  4218 characters
Sum:  1399
Retrieved:  4218 characters
Sum:  1476
Retrieved:  4218 characters
Sum:  1552
Retrieved:  4218 characters
Sum:  1627
Retrieved:  4218 characters
Sum:  1701
Retrieved:  4218 characters
Sum:  1773
Retrieved:  4218 characters
Sum:  1844
Retrieved:  4218 characters
Sum:  1913
Retrieved:  4218 characters
Sum:  1977
Retrieved:  4218 characters
Sum:  2040
Retrieved:  4218 characters
Sum:  2101
Retrieved:  4218 characters
Sum:  2162
Retrieved:  4218 characters
Sum:  2214
Retrieved:  4218 characters
Sum:  2262
Retrieved:  4218 characters
Sum:  2309
Retrieved:  4218 characters
Sum:  2346
Retrieved:  4218 characters
Sum:  2383
Retrieved:  4218 characters
Sum:  2416
Retrieved:  4218 characters
Sum:  2448
Retrieved:  4218 characters
Sum:  2480
Retrieved:  4218 characters
Sum:  2512
Retrieved:  4218 characters
Sum:  2543
Retrieved:  4218 characters
Sum:  2571
Retrieved:  4218 characters
Sum:  2597
Retrieved:  4218 characters
Sum:  2622
Retrieved:  4218 characters
Sum:  2638
Retrieved:  4218 characters
Sum:  2652
Retrieved:  4218 characters
Sum:  2665
Retrieved:  4218 characters
Sum:  2677
Retrieved:  4218 characters
Sum:  2688
Retrieved:  4218 characters
Sum:  2699
Retrieved:  4218 characters
Sum:  2709
Retrieved:  4218 characters
Sum:  2716
Retrieved:  4218 characters
Sum:  2721
Retrieved:  4218 characters
Sum:  2724'''


