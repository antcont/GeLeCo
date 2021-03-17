'''
A web scraper of texts and metadata from rechtsprechung-im-internet.de.

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
from bs4 import BeautifulSoup
from urllib3.util import Retry
import urllib3
import re
from xml.sax.saxutils import escape, unescape


retries = Retry(connect=15, read=10, redirect=15)
http = urllib3.PoolManager(retries=retries)

'''setting filepaths of input and output files'''
path_input = r""
path_output = r""

with open(path_input, "r") as f:
    mylist = f.read().splitlines()

len_list = len(mylist)
corpus_as_list = []

for id, url in enumerate(mylist):
    html = http.request('GET', url).data
    soup = BeautifulSoup(html, features="lxml")

    # getting/setting metadata
    type = "Gerichtsentscheidung"
    level = "Bund"
    database_URL = "rechtsprechung-im-internet.de"
    title_abbreviation = "NA"

    # getting title
    title_find = soup.find(class_="RspDL")
    if title_find:
        title = title_find.get_text(strip=True)
        title = escape(unescape(title))
        title = title.replace("\"", "&quot;")
        if "\n" in title:
            # to avoid newlines that would mess the XML tag; this happens when the court decision has no defined
            # title and the first sentence of the decision is caught by the script as "title"
            title = "NA"
        match = re.match(r"\d[A-ZÖÄÜ]", title) # if decision title begins with "1D" (es "1Der Kläger..."), set as NA
        if match:
            title = "NA"
    else:
        title = "NA"

    # getting drafting date
    drafting_date_match = re.search(r"Entscheidungsdatum:(.{8,10})", soup.get_text(strip=True))
    if drafting_date_match:
        drafting_date = drafting_date_match.group(1)
    else:
        drafting_date = "NA"

    # getting year
    year_match = re.search(r".+ ?(\d{4}$)", drafting_date)
    if year_match:
        year = year_match.group(1)
    else:
        year = "NA"

    # getting decade by slicing 7t to 9th character of drafting date and adding 0
    if drafting_date == "NA":
        decade = "NA"
    else:
        decade = drafting_date[6:9] + "0"

    # getting court detail
    court_detail_match = soup.find(string="Gericht:")
    if court_detail_match:
        court_detail = court_detail_match.next_element.get_text(strip=True)
        if "\n" in court_detail or len(court_detail) > 30:
            court_detail = "NA"
    else:
        court_detail = "NA"

    # getting court from court detail
    if court_detail == "NA":
        court = "NA"
    else:
        court_match = re.search(r"^(\w+) ", court_detail)
        if court_match:
            court = court_match.group(1)
        else:
            court = "NA"

    # getting reference
    reference_match = soup.find(string="Aktenzeichen:")
    if reference_match:
        reference = reference_match.next_element.get_text(strip=True)
    else:
        reference = "NA"

    # getting ECLI
    ECLI_match = soup.find(string="ECLI:")
    if ECLI_match:
        ECLI = ECLI_match.next_element.get_text(strip=True)
        if "\n" in ECLI:
            ECLI = "NA"
    else:
        ECLI = "NA"

    # getting decision_type (Dokumenttyp)
    decisiontype_match = soup.find(string="Dokumenttyp:")
    if decisiontype_match:
        decision_type = decisiontype_match.next_element.get_text(strip=True)
        if "\n" in decision_type:
            decision_type = "NA"
    else:
        decision_type = "NA"

    # building the <text> tag
    text_tag = '<text type="%s" level="%s" title="%s" title_abbreviation="%s" drafting_date="%s" decade="%s"' \
               ' database_URL="%s" court="%s" court_detail="%s" reference="%s" year="%s" decision_type="%s"' \
               ' ECLI="%s">' \
               % (type, level, title, title_abbreviation, drafting_date, decade, database_URL, court,
                  court_detail, reference, year, decision_type, ECLI)

    # scraping and adding the text body
    body = soup.get_text('\n', strip=True)

    # checking whether scraper has correctly navigated to the right URL or webpage does not contain any decision
    no_decision = "Das Bundesministerium der Justiz und für Verbraucherschutz und das Bundesamt für Justiz " \
                  "stellen für interessierte Bürgerinnen und Bürger ausgewählte Entscheidungen des" \
                  " Bundesverfassungsgerichts, der obersten Gerichtshöfe des Bundes sowie des" \
                  " Bundespatentgerichts ab dem Jahr 2010 kostenlos im Internet bereit."
    if no_decision in body:
        # discarding, exiting current loop and scraping next URL
        continue

    # adding <text> tag, body and closing tag
    corpus_as_list.append(text_tag)
    corpus_as_list.append(body)
    corpus_as_list.append("</text>")

    # printing progress
    print("\r", "%i out of %i scraped (%.2f%%)" % (id, len_list, (id/len_list*100)))

with open(path_output, "w+", encoding="utf-8") as file:
    file.write("\n".join(corpus_as_list))

print("Done.")





