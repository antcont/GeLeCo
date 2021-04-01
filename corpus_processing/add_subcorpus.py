'''
A script for adding a new (sentence-splitted, POS-tagged and lemmatized, xml) subcorpus to the master corpus
(add to the escaped xml version of the corpus).
A re-run of tagged2vert.py and unescape_s.py is necessary after adding the new subcorpus.
'''
import argparse
from lxml import etree
import gc
from pathlib import Path

gc.set_threshold(1000, 15, 15)      # setting higher thresholds for garbage collection, in order to avoid memory peaks
"

#  define cmd arguments
parser = argparse.ArgumentParser(description="A script for adding a subcorpus to the master corpus")
parser.add_argument("masterCorpus", help="the master corpus in xml format")
parser.add_argument("subCorpus", help="the master corpus in xml format")
args = parser.parse_args()

#  processing arguments
masterCorpus = args.masterCorpus
subCorpus = args.subCorpus


with open(masterCorpus, "r+", encoding="utf-8") as master_corpus:
    parser = etree.XMLParser(remove_blank_text=True, encoding='utf-8')
    tree_master = etree.parse(master_corpus, parser)
    root_master = tree_master.getroot()

    with open(subCorpus, "r+", encoding="utf-8") as subcorp:
        tree_subc = etree.parse(subcorp, parser)
        root_subc = tree_subc.getroot()
        for child in root_subc.getchildren():
            root_master.append(child)


filename_old = Path(masterCorpus).stem
filename_new = filename_old + "_subcorpus-added.xml"
tree_master.write(filename_new, encoding="utf-8")

print("Done")



