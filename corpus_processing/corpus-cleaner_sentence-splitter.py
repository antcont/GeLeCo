'''
A script for corpus cleaning and sentence splitting.

Input file is a raw-scraped corpus with <text> tags.
Cleaning:
- boilerplate lines are removed
Sentence splitting:
- lines with no period or one period are already considered sentences and not splitted, just tagged
- lines with two or more periods are sentence splitted using Kahn's and Schroeder's sentence-splitter
  (https://github.com/mediacloud/sentence-splitter) with a non-breaking prefixes file of legal abbreviations.


Output file is as follows (not a proper xml structure, root is missing and is added once the subcorpora are merged):

<text type="Gerichtsentscheidung" level="Bund" title="GmbH: Beschränkung der Stimmrechtsausübungsfreiheit eines
Gesellschafters aufgrund der Treuepflicht" title_abbreviation="NA" drafting_date="12.04.2016" decade="2010"
database_URL="rechtsprechung-im-internet.de" court="BGH" court_detail="BGH 2. Zivilsenat" reference="II ZR 275/14">
<s>
...
</s>
</text>

'''

from xml.sax.saxutils import escape, unescape
import re
from sentence_splitter import split_text_into_sentences
from yaspin import yaspin

raw_corpus = r""
path_output = r""

with open(raw_corpus, "r", encoding="utf-8") as file:
    lines = file.readlines()                                    # reading corpus per lines

len_lines = len(lines)

blacklist = ["zum Seitenanfang\n", "Datenschutz\n", "Barrierefreiheitserklärung\n", "Feedback-Formular\n",
             "Nichtamtliches Inhaltsverzeichnis\n", "Startseite\n", "Entscheidungssuche\n",
             "Benachrichtigungsdienst (RSS-Feed)\n", "Hinweise\n", "Impressum\n", "Rechtsprechung weiterer Gerichte\n",
             "Gesetze im Internet\n", "Verwaltungsvorschriften im Internet\n", "N-Lex\n", "Entscheidungssuche\n",
             "Suche\n", "Erweiterte Suche\n", "Tipps und Tricks\n", "Suchbegriffe\n", "Suche in\n",
             "Liste der auswählbaren Gerichte.\n", "Trefferliste\n", "Dokument\n", "XML\n", "PDF\n", "Kurztext\n",
             "Langtext\n", "Anlagen (nichtamtliches Verzeichnis)\n"]

tagged_corpus = []
with yaspin().bold.cyan.aesthetic as sp:  # printing spinner and % progress
    for id, line in enumerate(lines):
        if any(line == x for x in blacklist) or re.search(r"^Zurück zur Teilliste .+$", line):
            # ignoring boilerplate lines
            continue
        elif line == "</text>\n" or line.startswith("<text"):
            tagged_corpus.append(line.rstrip("\n"))
        # if line contains two or more period characters, we apply a sentence splitter
        elif line.count('.') >= 2:
            sentences = split_text_into_sentences(line, language="de", non_breaking_prefix_file="non-breaking-prefixes-german.txt")
            for sentence in sentences:
                tagged_corpus.append("<s>" + escape(unescape(sentence.rstrip("\n"))) + "</s>")
        else:
            tagged_corpus.append("<s>" + escape(unescape(line.rstrip("\n"))) + "</s>")
            if (id/200).is_integer(): #print % progress only each 200 iterations
                sp.text = "   %.2f%%" % (id/len_lines*100)

tagged_corpus_string = "\n".join(tagged_corpus)

with open(path_output, "w", encoding="utf-8") as file:
    file.write(tagged_corpus_string)

print("\nDone.")
