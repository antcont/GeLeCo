# GeLeCo: A large German Legal Corpus of laws, administrative regulations and court decisions published in Germany until 2020.

## Documentation

### 1.  Introduction
The GeLeCo corpus is a large German Legal Corpus for research, teaching and translation purposes. It includes the complete collection of federal laws, administrative regulations and court decisions which have been published on three online databases by the German Federal Ministry of Justice and Consumer Protection and the Federal Office of Justice (`www.gesetze-im-internet.de`, `www.verwaltungsvorschriften-im-internet.de`, `www.rechtsprechung-im-internet.de`).

### 2.	Corpus design
#### 2.1.	Composition

| text type |	database URL | text count	| token count |
| :--------- | :--------- | :---------: | :---------: |
|laws |	gesetze-im-internet.de |	6,577	| 22,502,937 |
|court decisions |	rechtsprechung-im-internet.de |	55,361	| 167,210,730 |
|administrative regulations |	verwaltungsvorschriften-im-internet.de |	787	| 3,469,166 |
|**total count** |  |	**62,725** |	**193,182,833** |

The largest subcorpus (the corpus of court decisions published on `www.rechtsprechung-im-internet.de`) has the following composition: 
| issuing court | text count | % |
| :------- | :------: | :------: |
| Bundesarbeitsgericht (BAG) | 5,697 | 10,3% |
| Bundesfinanzhof (BFH) | 8,964 | 16,2% |
| Bundesgerichtshof (BGH) | 19,069 | 34,4% |
| Bundespatentgericht (BPatG) | 5,913 | 10,7% |
| Bundessozialgericht (BSG) | 4,460 | 8,1 % |
| Bundesverfassungsgericht (BVerfG) | 3,878 | 7,0% |
| Bundesverwaltungsgericht (BVerwG) | 7,189 | 13,9% |
| NA | 191 | 0,3% |
| **total** | **55,361** | **100,0%** |


#### 2.2.	Annotation scheme
The corpus has been compiled in vertical or word-per-line (WPL) format as required by SketchEngine and NoSketchEngine. It has been marked-up with contextual (metadata), structural (text and sentence boundaries) and linguistic (POS tagging, lemmatisation) annotation (s. below). The complete POS tagset is available on [spacy.io](https://spacy.io/api/annotation#pos-de). 

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


#### 2.3.	Metadata
Contextual information marked-up for each text includes:
-	`title`
-	`title_abbreviation`
-	`type`: can take one of the following values: _Gesetz_ (law), _Gerichtsentscheidung_ (court decision), _Verwaltungsvorschrift_ (administrative regulation)
-	`level`: indicates whether the law, regulation or court decision was published at federal or _Länder_ level. This metadate has been included with sight to a possible extension of the corpus to laws, regulations and court decisions published at _Länder_ level. It can take the following values: 
    -	_Bund_: federal level
    -	_Land_: _Länder_ level (not present in this corpus)
-	`drafting_date`: this corresponds to the _Ausfertigungsdatum_ of laws and the _Entscheidungsdatum_ of court decisions.
-	`year`
-	`decade`
-	`database_URL`: can take the following values: _gesetze-im-internet.de_, _rechtsprechung-im-internet.de_, _verwaltungsvorschriften-im-internet.de_
-	`court`
-	`court_detail`
-	`reference`: a reference code for court decisions (_Aktenzeichen_)
-	`decision_type`: the type of document for court decisions (_Dokumenttyp_) 
-	`ECLI`: the European Case Law Identifier code for court decisions.


### 3.	Corpus building steps
##### 3.1.	URL collection
All URLs were collected by means of website-specific web scrapers written in Python. Three lists of URLs were exported in newline-separated .txt files for subsequent text scraping.

#### 3.2.	Text scraping and XML tagging
Based on the previously collected URL lists, single legal texts were scraped by means of custom web scrapers written in Python. Text and metadata collection was carried out using the BeautifulSoup Python library. Text contained in different HTML tags has been newline-separated, making the subsequent sentence splitting stage easier and faster to carry out. After scraping, texts have been merged and a first raw corpus version has been exported as a single .txt file for each subcorpus.

#### 3.3.	Boilerplate cleaning, deduplication, text filtering
Boilerplate lines have been eliminated by means of regular expressions. Texts extracted from not correctly visualized webpages (not containing any law, regulation or court decision) have been discarded. Texts have also been deduplicated based on metadata equivalence.

#### 3.4.	Sentence splitting
After scraping and cleaning, the subcorpora have been sentence splitted. In particular, only lines containing two or more period characters have undergone sentence splitting. I used [Kahn’s and Schroeder’s sentence-splitter](https://github.com/mediacloud/sentence-splitter) adding a list of non-breaking prefixes with legal abbreviations taken from the corpus and from online sources. After splitting, lines have been added opening and closing sentence delimiting tags (`<s>`).

#### 3.5.	POS tagging and lemmatization
The corpus has been tagged with Part-of-Speech tags and lemmas. This was carried out using the SpaCy tagger.  The output has not undergone any systematic revision or correction stage; therefore, the corpus may contain minor sentence splitting or annotation errors.

### 4.  Possible uses of the corpus and further development
The GeLeCo corpus can be used for several purposes: research in the field of diachronic or synchronic, monolingual or comparative legal corpus linguistics or discourse analysis, translator training and translation practice, legal lexicography and terminography, as well as Natural Language Processing (NLP) applications.
Potential future development includes the extension of the corpus by scraping other publicly available databases containing laws, court decisions and/or administrative regulations issued at _Länder_ level. Each _Land_ has its own databases whose texts can be easily scraped by means of customized Python scripts; the extended corpus could potentially reach a huge size of several hundreds of millions of tokens.
