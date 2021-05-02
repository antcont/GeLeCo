'''
A web scraper to collect all URLs from verwaltungsvorschriften-im-internet.de.
'''

import argparse
import urllib3
from bs4 import BeautifulSoup
import re
from urllib3.util import Retry

#  define cmd arguments
parser = argparse.ArgumentParser(description="A web scraper to collect all URLs from"
                                             " verwaltungsvorschriften-im-internet.de."
                                             "\nA .txt file containing the list is created in the same folder.")
args = parser.parse_args()


url_domain = "http://www.verwaltungsvorschriften-im-internet.de/"

retries = Retry(connect=5, read=2, redirect=5)
http = urllib3.PoolManager(retries=retries)

#  getting URLs to each subdirectory, in the id="container" section
html = http.request('GET', "http://www.verwaltungsvorschriften-im-internet.de/erlassstellen.html").data
soup = BeautifulSoup(html, features="lxml")
list_subdirectories = []
section = soup.find(id="container")

for link in section.find_all("a"):
    href = link.get('href')
    match = re.match(r"\./(Teilliste_.+\.html)", href)
    clean = match.group(1)
    url_clean_coll = url_domain + clean
    list_subdirectories.append(url_clean_coll)

#  getting all URLs from each subdirectory
URL_list = []
for x in list_subdirectories:
    html = http.request('GET', x).data
    soup = BeautifulSoup(html, features="lxml")
    section = soup.find(id="container")

    for link in section.find_all("a"):
        href = link.get('href')
        if href:
            match = re.match(r"\./(.+\.htm)", href)
            if match is None:
                #print(href)
                continue
            clean = match.group(1)
            url_clean_law = url_domain + clean
            URL_list.append(url_clean_law)


#  writing URL list
with open("URL_list_V.txt", "w", encoding="utf-8", newline="\n") as file:
    file.write("\n".join(URL_list))

print("Done.")