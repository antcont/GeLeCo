'''
Tokenization, POS tagging and lemmatization using the TreeTagger.

Input: sentence splitted XML corpus.
Output: tokenized, POS tagged and lemmatized corpus (still not properly vertical, use tagged2vert.py).
'''
import treetaggerwrapper
from lxml import etree
import gc

gc.set_threshold(1000, 15, 15)      # setting higher thresholds for garbage collection, in order to avoid memory peaks

'''setting up TreeTagger wrapper'''
tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')

'''setting filepaths for input and output files'''
path_input = r""
path_output = r""

counter = 0
with open(path_input, 'r+', encoding='utf-8') as file:
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

tree.write(path_output, encoding="utf-8")

print("Done")