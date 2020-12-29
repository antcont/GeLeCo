# GeLeCo
## A large German Legal Corpus of laws, administrative regulations and court decisions published in Germany until 2020.


### 1.	Corpus design
#### 1.1.	Composition

| text type |	database URL | text count	| token count |
| :--------- | :--------- | :---------: | :---------: |
|laws |	gesetze-im-internet.de |	6586	| 22,626,473 |
|court decisions |	rechtsprechung-im-internet.de |	57945	| 168,441,219 |
|administrative regulations |	verwaltungsvorschriften-im-internet.de |	813	| 3,519,344 |
|total count |  |	**65,344** |	**194,587,036** |


#### 1.2.	Metadata
Metadata extracted for each text include:
-	_title_
-	_title_abbreviation_
-	_type_: can take one of the following values:
    - _Gesetz_ (law)
    -	_Gerichtsentscheidung_ (court decision) 
    -	_Verwaltungsvorschrift_ (administrative regulation)
-	_level_: indicates whether it is a law/regulation at a national or regional level, or whether the court decision was taken by a national or regional court. Even though this corpus contains only national-level laws, regulations and decisions, this metadate has been included with sight to a possible extension of the corpus to regional legal texts. It can take the following values:
    -	_Bund_: national level
    -	_Land_: regional level (not present in this corpus)
-	_drafting_date_: this corresponds to the Ausfertigungsdatum of laws and the Entscheidungsdatum of court decisions.
-	_year_
-	_decade_
-	_database_URL_: can take the following values:
    -	_gesetze-im-internet.de_
    -	_rechtsprechung-im-internet.de_
    -	_verwaltungsvorschriften-im-internet.de_
-	_court_
-	_court_detail_
-	_reference_: a reference code for court decisions (Aktenzeichen)
-	_decision_type_: the type of document for court decisions (Dokumenttyp) 
-	_ECLI_: the European Case Law Identifier code for court decisions.




#### 1.3.	Annotation scheme
The corpus has been compiled in vertical format as required by SketchEngine and NoSketchEngine. The corpus has been annotated with XML tags at corpus, text and sentence level (s. below). At the token level, it has been annotated with Part-of-Speech tags and lemmas. The complete POS tagset is available on spacy.io. 

```
<corpus>
<text type="Gerichtsentscheidung" level="Bund" title="GmbH: Beschränkung der Stimmrechtsausübungsfreiheit eines Gesellschafters aufgrund der Treuepflicht" title_abbreviation="NA" drafting_date="12.04.2016" decade="2010" database_URL="rechtsprechung-im-internet.de" court="BGH" court_detail="BGH 2. Zivilsenat" reference="II ZR 275/14" year="2016" decision_type="Urteil" ECLI="ECLI:DE:BGH:2016:120416UIIZR275.14.0">
<s>
Nach	ADP	Nach
dem	DET	der
1.	ADJ	1.
April	NOUN	April
1941	NUM	1941
werden	AUX	werden
Gewinnausschüttungen	NOUN	Gewinnausschüttungen
von	ADP	von
Versorgungsunternehmen	NOUN	Versorgungsunternehmen
an	ADP	an
Gemeinden	NOUN	Gemeinde
anerkannt	VERB	anerkennen
.	PUNCT	.
</s>
</text>
</corpus>
```


### 2.	Corpus building steps
2.1.	URL collection
All URLs were collected by means of website-specific web scrapers written on Python. Three lists of URLs were exported in newline-separated .txt files for subsequent text scraping.

#### 2.2.	Text scraping and XML tagging
Based on the previously collected URL lists, single legal texts were scraped with custom web scrapers written in Python. Text and metadata collection was carried out using the BeautifulSoup library. 
Text contained in different tags has been newline-separated, making the following sentence splitting stage easier and faster to carry out. After scraping, texts have been merged and a first raw corpus version has been exported as a single .txt file for each subcorpus.

#### 2.3.	Boilerplate cleaning
Boilerplate lines have been filtered out by means of regular expressions.

#### 2.4.	Sentence splitting
After scraping and cleaning, the subcorpora have been sentence splitted. In particular, only lines containing two or more period characters have undergone sentence splitting. I used Kahn’s and Schroeder’s sentence-splitter  adding a list of non-breaking prefixes with legal abbreviations taken from the corpus and from online sources. After splitting, lines have been added opening and closing sentence delimiting tags (`<s>`).

#### 2.5.	POS tagging and lemmatization
The corpus has been tagged with Part-of-Speech tags and lemmas. This was carried out using the SpaCy model.  The output has not undergone any extensive revision or correction; therefore, the corpus may contain minor sentence splitting or tagging errors.


