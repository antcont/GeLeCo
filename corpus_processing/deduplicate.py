'''
A script for text deduplication, based on metadata equivalence.
'''
import argparse
from lxml import etree
from pathlib import Path


#  define cmd arguments
parser = argparse.ArgumentParser(description="A script for text deduplication, based on metadata equivalence.")
parser.add_argument("corpus", help="the corpus in .xml format to be deduplicated")
parser.add_argument("-o", "--overwrite", help="(optional) overwriting the old corpus; by default, a new file is created",
                    action="store_true")
args = parser.parse_args()

#  processing arguments
inputCorpus = args.corpus
overwrite = args.overwrite


with open(inputCorpus, "r+", encoding="utf-8") as corp:
    parser = etree.XMLParser(encoding='utf-8')
    tree = etree.parse(corp, parser)
    print("Corpus parsed. Now processing attributes...")
    root = tree.getroot()
    attributes = []
    for text in root.findall("text"):
        attributes.append(text.attrib)      # a list of dictionaries of attributes, not deduplicated

    #  this way the list of dicts of attributes has the same order even after deduplication (set)
    #  and comparison with attributes of single texts is less computationally expensive
    unique_sets = set(frozenset(d.items()) for d in attributes)
    dedupl = [dict(s) for s in unique_sets]

    #  this list is the deduplicated list of attributes against which each text will be compared
    dedupl.append({"just": "because", "this": "way", "it's": "never", "empty": "!!"})  # this is done in order for
                                                                    # the list to not be empty in the last iterations
    print("List of dictionaries of attributes collected")

    #  removing duplicates by comparing attributes (metadata)
    counter_texts = 0
    counter_removed = 0
    for text in root.findall("text"):
        counter_texts += 1
        attribs = text.attrib
        for x in dedupl:
            dupl = True
            if attribs == x:
                dedupl.remove(x)
                dupl = False
                break
        if dupl:
            root.remove(text)
            counter_removed += 1

        print("\r", "%i texts out of 65000 (%.2f%%) checked for deduplication" % (counter_texts, (counter_texts/65000*100)), end="")

print("%i texts eliminated. Now writing..." % counter_removed)

if overwrite:
    tree.write(inputCorpus, encoding="utf-8")
else:  # overwrite == False (default)
    filename_old = Path(inputCorpus).stem
    filename_new = filename_old + "_deduplicated.xml"
    tree.write(filename_new, encoding="utf-8")


print("\rDone")



