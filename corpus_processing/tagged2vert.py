'''
A script for the cleaning and final verticalization of the corpus as a word-per-line (WPL) file.
The output .vert file has the following structure:

<corpus>
<text type="Gerichtsentscheidung" level="Bund" title="GmbH: Beschränkung der Stimmrechtsausübungsfreiheit eines
Gesellschafters aufgrund der Treuepflicht" title_abbreviation="NA" drafting_date="12.04.2016" decade="2010"
database_URL="rechtsprechung-im-internet.de" court="BGH" court_detail="BGH 2. Zivilsenat" reference="II ZR 275/14"
year="2016" decision_type="Urteil" ECLI="ECLI:DE:BGH:2016:120416UIIZR275.14.0">
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
'''
import re
import gc
from yaspin import yaspin
from xml.sax.saxutils import unescape


gc.set_threshold(1000, 15, 15)      # setting higher thresholds for garbage collection, in order to avoid memory peaks

#set input and output filepaths
fileXML = r""
path_output = r""

regex_list = [                              #create a list of regex to clean up the text and split tags
    (r'(>)(<)', r'\1\r\n\2'),
    (r'(</s>)', r'\r\n\1'),
    (r'(<s>)', r'\1\r\n'),
    (r'.+\tSPACE\t.+$', r''),               #remove lines with tagged spaces
    (r'(\r\n|\r\r\n)', r'\n')
]

with open(fileXML, 'r+', encoding='utf-8') as file:
    corpus = file.readlines()
    print("Managed to read corpus.")

    with open(path_output, "w+", encoding="utf-8") as corpus_vert:
        with yaspin().bold.cyan.aesthetic as sp:                # printing spinner and % progress
            lines_counter = 0
            for line in corpus:
                for to_find, to_replace in regex_list:
                    line = re.sub(to_find, to_replace, line)    # apply all regexes to the string
                if not line.startswith("<"):   #unescaping
                    line = unescape(line)
                    line = line.replace("&quot;", "\"")
                if line != "\n" and line != "\r\n":            # ignore empty lines
                    corpus_vert.write(line)
                    lines_counter += 1
                    if (lines_counter/10000).is_integer():       # refresh counter each 10000 tokens
                        sp.text = "%i lines written" % lines_counter

print("Done")






