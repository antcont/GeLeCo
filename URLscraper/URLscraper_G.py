'''
A web scraper to collect all URLs from gesetze-im-internet.de.
'''

import urllib3
from bs4 import BeautifulSoup
import re
from urllib3.util import Retry

retries = Retry(connect=5, read=2, redirect=5)
http = urllib3.PoolManager(retries=retries)

url_domain = "https://www.gesetze-im-internet.de/"

'''set filepaths for output file'''
path_output = r""

'''laws are organized alphabetically: colleting URLs for each letter's subdirectory'''
r = http.request('GET', "https://www.gesetze-im-internet.de/aktuell.html")
html = r.data
soup = BeautifulSoup(html, features="lxml")
lista_pagine_alfab = []
section = soup.find(id="container")
for link in section.find_all("a"):
    href = link.get('href')
    match = re.match(r"\./(Teilliste_.\.html)", href)
    clean = match.group(1)
    url_clean_coll = url_domain + clean
    lista_pagine_alfab.append(url_clean_coll)


'''collecting proper list of law URLs'''
URL_laws = []
for x in lista_pagine_alfab:
    r = http.request('GET', x)
    html = r.data
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

'''for each URL, navigate to the URL and get the URL to the full "HTML" version of the law'''
lista_URL_html = []
counter = 0
for x in URL_laws:
    parts = x.split('/')
    parts.pop()
    url_part = "/".join(parts)
    r = http.request('GET', x)
    html = r.data
    soup = BeautifulSoup(html, features="lxml")
    section = soup.find(id="container")
    a_string = section.find(string="HTML")
    a = a_string.find_parent("a")
    href = a.get('href')
    if href is None:
        continue
    url_clean_html = url_part + "/" + href
    lista_URL_html.append(url_clean_html)
    counter += 1
    print("\r", "%i out of 6550 URLs scraped (%.2f%%)" % (counter, (counter/6550*100)), end="")

URLs = "\n".join(lista_URL_html)

with open(path_output, "w", encoding="utf-8") as file:
    file.write(URLs)


