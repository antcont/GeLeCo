'''
A web scraper to collect all URLs from gesetze-im-internet.de.
'''

import argparse
import urllib3
from bs4 import BeautifulSoup
import re
from urllib3.util import Retry

retries = Retry(connect=5, read=2, redirect=5)
http = urllib3.PoolManager(retries=retries)

#  define cmd arguments
parser = argparse.ArgumentParser(description="A web scraper to collect all URLs from gesetze-im-internet.de."
                                             "\nA .txt file containing the list is created in the same folder.")
args = parser.parse_args()


url_domain = "https://www.gesetze-im-internet.de/"

#  laws are organized alphabetically: colleting URLs for each letter's subdirectory
html = http.request('GET', "https://www.gesetze-im-internet.de/aktuell.html").data
soup = BeautifulSoup(html, features="lxml")
lista_pagine_alfab = []
section = soup.find(id="container")

for link in section.find_all("a"):
    href = link.get('href')
    match = re.match(r"\./(Teilliste_.\.html)", href)
    clean = match.group(1)
    url_clean_coll = url_domain + clean
    lista_pagine_alfab.append(url_clean_coll)


#  collecting proper list of law URLs
URL_laws = []
for x in lista_pagine_alfab:
    html = http.request('GET', x).data
    soup = BeautifulSoup(html, features="lxml")
    section = soup.find(id="container")

    for link in section.find_all("a"):
        href = link.get('href')
        match = re.match(r"\./(.+\.html)", href)

        if match is None:
            continue
        clean = match.group(1)
        url_clean_law = url_domain + clean
        URL_laws.append(url_clean_law)


#  for each URL, navigate to the URL and get the URL to the full "HTML" version of the law
URL_list = []
counter = 0

for x in URL_laws:
    parts = x.split('/')
    parts.pop()                                 # removing final part of URL "/index.html"
    url_part = "/".join(parts)                  # merging URL after removing "/index.html"
    html = http.request('GET', x).data
    soup = BeautifulSoup(html, features="lxml")
    section = soup.find(id="container")
    a_string = section.find(string="HTML")
    a = a_string.find_parent("a")
    href = a.get('href')
    if href is None:
        continue
    url_clean_html = url_part + "/" + href      # adding local href to build the final URL
    URL_list.append(url_clean_html)
    counter += 1

    print("\r", "%i URLs scraped" % counter, end="")


#  writing URL list
with open("URL_list_G.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(URL_list))

print("Done.")