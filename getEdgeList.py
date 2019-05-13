"""
    getEdgeList.py

    scrape all request for adminship pages for voting histories
"""

import requests
import re
from bs4 import BeautifulSoup
import csv
import pandas as pd


S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

result = []
df = pd.read_csv('csvfile.csv', names=['pageId', 'timestamp'])
df = df['pageId'].tolist()

count = 0
for i in df:

    PARAMS = {
        'action': "parse",
        'pageid': int(i),
        'format': "json",
        "prop": "text"
    }

    R = S.get(url=URL, params=PARAMS)
    soup = BeautifulSoup(R.json()["parse"]["text"]["*"], 'lxml')

    if soup.h3 is not None:
        title = soup.h3.span['id']
    else:
        title = 'NA'

    if soup.find(text='Support') is not None:
        if soup.find(text='Support').findNext('ol') is not None:
            support = soup.find(text='Support').findNext('ol').find_all('a', title=re.compile("^User:"))
            for j in support:
                result.append([title, j['title'][5:], 1])
    else:
        result.append([title, 'NA', 1])

    if soup.find(text='Oppose') is not None:
        if soup.find(text='Oppose').findNext('ol') is not None:
            oppose = soup.find(text='Oppose').findNext('ol').find_all('a', title=re.compile("^User:"))
            for k in oppose:
                result.append([title, k['title'][5:], -1])
    else:
        result.append([title, 'NA', -1])

with open("edgelist.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(result)
