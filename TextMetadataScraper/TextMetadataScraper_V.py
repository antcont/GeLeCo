'''
A web scraper of texts and metadata from verwaltungsvorschriften-im-internet.de.

Input file is a newline-separated .txt file of URLs.
The output from this initial scraping is like the following, for each text:

<text type="Gerichtsentscheidung" level="Bund" title="Konkurrenzverhältnis bei Betrug: Einreichung mehrerer
Kreditanträge am selben Tag bei demselben Bankinstitut ohne Rückzahlungswillen" title_abbreviation="NA"
drafting_date="23.06.2016" decade="2010" database_URL="rechtsprechung-im-internet.de" court="BGH"
court_detail="BGH 4. Strafsenat" reference="4 StR 75/16" year="2016" decision_type="Beschluss"
ECLI="ECLI:DE:BGH:2016:230616B4STR75.16.0">
...
</text>

The output is one single .txt file of all texts, each with a <text> tag and metadata.
'''
import argparse
from bs4 import BeautifulSoup
from urllib3.util import Retry
import urllib3
import re
from xml.sax.saxutils import escape, unescape

retries = Retry(connect=5, read=2, redirect=5)
http = urllib3.PoolManager(retries=retries)


#  define cmd arguments
parser = argparse.ArgumentParser(description="A web scraper of texts and metadata from"
                                             " verwaltungsvorschriften-im-internet.de.")
parser.add_argument("urlList", help="a .txt file of newline-separated URLs to be scraped")
args = parser.parse_args()

#  processing arguments
urlList = args.urlList


with open(urlList, "r") as f:
    mylist = f.read().splitlines()

corpus_as_list = []

for id, url in enumerate(mylist):
    html = http.request('GET', url).data
    soup = BeautifulSoup(html, features="lxml")

    #  getting/setting metadata
    type = "Verwaltungsvorschrift"
    level = "Bund"
    database_URL = "verwaltungsvorschriften-im-internet.de"
    court = "NA"
    court_detail = "NA"
    reference = "NA"
    decision_type = "NA"
    ECLI = "NA"

    #  getting title and abbreviation (if any)
    titlex = soup.find("title").get_text(strip=True)
    # abbreviation can be found at the end of the title, between parentheses, sometimes followed by the drafting date
    title_match = re.search(r"^(.+) ?\((.+)\)( (vom|v\.) (\d\d?\.\d\d?\.\d\d\d\d|\d\d?\. \w{3,10} \d\d\d\d))? ?$",
                            titlex)
    if title_match: # matching titles with final parenthesis containing the abbreviation
        title = title_match.group(1)
        title_abbreviation = title_match.group(2)
        title_abbreviation = escape(unescape(title_abbreviation))
        title_abbreviation = title_abbreviation.replace("\"", "&quot;")
    else: #if title has not a final parenthesis with the abbreviation
        title = titlex
        title_abbreviation = "NA"
    title = escape(unescape(title))
    title = title.replace("\"", "&quot;")

    #  getting drafting_date from the title. unfortunately, there is no other specific section
    #  where the drafting_date is to be found coherently
    match_date = re.search(r"^.+(vom|v\.) (\d\d?\.\d\d?\.\d\d\d\d|\d\d?\. \w{3,10} \d\d\d\d) ?(\(.+\))?$", titlex)
    if match_date:
        drafting_date = match_date.group(2)
    else:
        drafting_date = "NA"

    #  getting decade and year
    if drafting_date == "NA":
        decade = "NA"
        year = "NA"
    else:
        match_decade = re.search(r"((\d\d\d)\d)$", drafting_date)
        decade = match_decade.group(2) + "0"
        year = match_decade.group(1)

    #  building the <text> tag
    text_tag = '<text type="%s" level="%s" title="%s" title_abbreviation="%s" drafting_date="%s" decade="%s" database_URL="%s" court="%s" court_detail="%s" reference="%s" year="%s" decision_type="%s" ECLI="%s">' % (type, level, title, title_abbreviation, drafting_date, decade, database_URL, court, court_detail, reference, year, decision_type, ECLI)
    corpus_as_list.append(text_tag)

    #  scraping and adding the text body
    body = soup.get_text('\n', strip=True)
    corpus_as_list.append(body)

    #  adding the </text> closing tag
    corpus_as_list.append("</text>")

    #  printing progress
    print("\r", "%i out of %i (%.2f%%)" % (id, len(mylist), (id/(len(mylist))*100)), end="")


#  writing corpus as a single txt file
with open("corpus_V.txt", "w+", encoding="utf-8") as corpus:
    corpus.write("\n".join(corpus_as_list))

print("\rDone")