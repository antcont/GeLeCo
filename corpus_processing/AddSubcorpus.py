'''
A script for adding a new (sentence-splitted, POS-tagged and lemmatized) subcorpus to the master corpus.
A re-run of tagged2vert.py is necessary after adding the new subcorpus.
'''

from lxml import etree
import gc
gc.set_threshold(1000, 15, 15)      # setting higher thresholds for garbage collection, in order to avoid memory peaks

#setting filepaths
master_corpus = r""
subcorpus = r""
master_corpus_out = r""

with open(master_corpus, "r+", encoding="utf-8") as master_corpus:
    parser = etree.XMLParser(remove_blank_text=True, encoding='utf-8')
    tree_master = etree.parse(master_corpus, parser)
    root_master = tree_master.getroot()

    with open(subcorpus, "r+", encoding="utf-8") as subcorp:
        tree_subc = etree.parse(subcorp, parser)
        root_subc = tree_subc.getroot()
        for child in root_subc.getchildren():
            root_master.append(child)

tree_master.write(master_corpus_out, encoding="utf-8")

print("Done")



