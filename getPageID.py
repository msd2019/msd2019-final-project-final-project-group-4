"""
    getPageID.py

    Scrape out all pages of Request for Adminship attempts
"""
import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS_INIT = {
    'action': "query",
    'list': "categorymembers",
    'cmtitle': "Category:Successful requests for adminship",
    'cmlimit': 500,
    'cmsort' : 'timestamp',
    'format': "json",
    'cmprop': 'ids|timestamp'
}

#run first query to retrieve 'cmcontinue' value, write frist 500 id's to file
R = S.get(url=URL, params=PARAMS_INIT)
DATA = R.json()

with open('csvfile.csv', 'w') as file:
    for i in DATA['query']['categorymembers']:
        file.write(str(i['pageid'])+ ','+ str(i['timestamp']) + '\n')

#hand-collected 'cmcontinue' values
df = ['2007-12-11 23:26:22|14555606', '2009-06-10 14:19:37|2294211', '2009-06-10 17:54:17|4358913','2013-05-09 10:40:49|39277059']

for i in df:
    PARAMS = {
            'action': "query",
            'list': "categorymembers",
            'cmtitle': "Category:Successful requests for adminship",
            'cmlimit': 500,
            'cmcontinue': str(i),
            'cmsort': 'timestamp',
            'format': "json",
            'cmprop': 'ids|timestamp'
        }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    print(DATA)

    with open('pageids.csv', 'a') as file:
        for j in DATA['query']['categorymembers']:
            file.write(str(j['pageid'])+ ','+ str(j['timestamp']) + '\n')
