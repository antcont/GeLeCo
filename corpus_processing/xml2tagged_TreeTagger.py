'''
Tokenization, POS tagging and lemmatization using the TreeTagger.

TreeTagger needs to be installed.

Input: sentence splitted XML corpus.
Output: tokenized, POS tagged and lemmatized corpus
        Output is still not properly vertical, use tagged2vert.py (separately for RAM reasons).
'''
import argparse
import treetaggerwrapper
from lxml import etree
import gc
from pathlib import Path

gc.set_threshold(1000, 15, 15)      # setting higher thresholds for garbage collection, in order to avoid memory peaks


#  setting up TreeTagger wrapper
tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')

#  define cmd arguments
parser = argparse.ArgumentParser(description="A script for tokenization, lemmatization and POS tagging using the TreeTagger")
parser.add_argument("corpus", help="the corpus in .xml format to be tagged")
parser.add_argument("-o", "--overwrite", help="(optional) overwriting the old corpus; by default, a new file is created",
                    action="store_true")
args = parser.parse_args()

#  processing arguments
inputCorpus = args.corpus
overwrite = args.overwrite

counter = 0

with open(inputCorpus, 'r+', encoding='utf-8') as file:
    parser = etree.XMLParser(remove_blank_text=True, encoding='utf-8')
    tree = etree.parse(file, parser)
    print("Corpus parsed. Now tagging...")

    for element in tree.iter():
        if element.text is not None:
            tags = tagger.tag_text(element.text)
            for tag in tags:
                counter += 1
            element.text = "\n".join(tags)
            if (counter/1000).is_integer():
                print("\r", "%.2f%%" % ((100*counter)/200000000), end="")


if overwrite:
    tree.write(inputCorpus, encoding="utf-8")

else:  # if overwrite == False (default)
    filename_old = Path(inputCorpus).stem
    filename_new = filename_old + "_taggedTreeTagger.xml"
    tree.write(filename_new, encoding="utf-8")


print("Done")