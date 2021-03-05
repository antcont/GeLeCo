'''
Tokenization, POS tagging and lemmatization using SpaCy.

Input: sentence splitted XML corpus.
Output: tokenized, POS tagged and lemmatized corpus (still not properly vertical, use tagged2vert.py).

SpaCy's .pos_ adds UPOS coarse-grained tags (use .tag for fine-grained POS tagging)
'''

from lxml import etree
import spacy
import gc
from yaspin import yaspin

gc.set_threshold(1000, 15, 15)      # setting higher thresholds for garbage collection, in order to avoid memory peaks

'''loading German model to SpaCy'''
nlp = spacy.load("de_core_news_lg")

'''setting filepaths for input and output files'''
path_input = r""
path_output = r""

with open(path_input, 'r+', encoding='utf-8') as file:
    parser = etree.XMLParser(remove_blank_text=True, encoding='utf-8')
    tree = etree.parse(file, parser)
    print("Corpus parsed. Now tagging...")

    with yaspin().bold.cyan.aesthetic as sp:                    # printing spinner and % progress
        counter = 0
        for element in tree.iter():                             # iterate over each tag element
            if element.text is not None:
                doc = nlp(element.text, disable=['parser', 'ner']) # parse the text with SpaCy
                segm = list()                                   # create a list for the single <s> segments
                for w in doc:                                   # iterate over each word in the segment
                    if w.text != '\n' and w.text != '\r' and w.text != '\r\n':  # ignore newline characters
                        # building tab-separated line for vert file (token-POS-lemma)
                        # (use w.tag for fine-grained POS tagging)
                        segm.append(f"""{w.text}\t{w.pos_}\t{w.lemma_}""")
                        counter += 1
                        if (counter/1000).is_integer():
                            sp.text = "%i out of approx 200358000 tokens tagged (%.2f%%)"\
                                      % (counter, counter/200358000*100)

                element.text = "\n".join(segm)

tree.write(path_output, encoding="utf-8")

print("Tokens written: ", counter)
print("Done")



