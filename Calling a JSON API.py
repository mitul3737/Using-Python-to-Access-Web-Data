#API End Points by Mitul
import urllib.error, urllib.request, urllib.parse
import json

target = 'http://py4e-data.dr-chuck.net/json?'
local = input('Enter location: ')
url = target + urllib.parse.urlencode({'address': local, 'key' : 42})

print('Retriving', url)
data = urllib.request.urlopen(url).read()
print('Retrived', len(data), 'characters')
js = json.loads(data)
print(json.dumps(js, indent = 4))
print('Place id', js['results'][0]['place_id'])


'''Output:
Enter location: >? UIUC
Retriving http://py4e-data.dr-chuck.net/json?address=UIUC&key=42
Retrived 1720 characters
{
    "results": [
        {
            "access_points": [],
            "address_components": [
                {
                    "long_name": "Champaign",
                    "short_name": "Champaign",
                    "types": [
                        "locality",
                        "political"
                    ]
                },
                {
                    "long_name": "Champaign County",
                    "short_name": "Champaign County",
                    "types": [
                        "administrative_area_level_2",
                        "political"
                    ]
                },
                {
                    "long_name": "Illinois",
                    "short_name": "IL",
                    "types": [
                        "administrative_area_level_1",
                        "political"
                    ]
                },
                {
                    "long_name": "United States",
                    "short_name": "US",
                    "types": [
                        "country",
                        "political"
                    ]
                }
            ],
            "formatted_address": "Champaign, IL, USA",
            "geometry": {
                "location": {
                    "lat": 40.1019523,
                    "lng": -88.2271615
                },
                "location_type": "GEOMETRIC_CENTER",
                "viewport": {
                    "northeast": {
                        "lat": 40.1033012802915,
                        "lng": -88.22581251970848
                    },
                    "southwest": {
                        "lat": 40.1006033197085,
                        "lng": -88.2285104802915
                    }
                }
            },
            "place_id": "ChIJ6VUmqSTXDIgR-iZoBCUFPKU",
            "plus_code": {
                "compound_code": "4Q2F+Q4 Champaign, Champaign City Township, IL, United States",
                "global_code": "86GH4Q2F+Q4"
            },
            "types": [
                "establishment",
                "point_of_interest",
                "university"
            ]
        }
    ],
    "status": "OK"
}
Place id ChIJ6VUmqSTXDIgR-iZoBCUFPKU
'''
