'''
A script for merging the three subcorpora and adding the <corpus> root tag.
'''
import argparse


#  define cmd arguments
parser = argparse.ArgumentParser(description="A script for merging the three subcorpora and adding a root element")
parser.add_argument("corpus1", help="the subcorpus in .xml format to be merged")
parser.add_argument("corpus2", help="the subcorpus in .xml format to be merged")
parser.add_argument("corpus3", help="the subcorpus in .xml format to be merged")
args = parser.parse_args()

#  processing arguments
inputCorpus1 = args.corpus1
inputCorpus2 = args.corpus2
inputCorpus3 = args.corpus3


merged_corpus = ["<corpus>"]

with open(inputCorpus1, "r", encoding="utf-8") as file:
    lines = file.readlines()
for line in lines:
    if line != "\n" or line != "\r\n":
        merged_corpus.append(line)

with open(inputCorpus2, "r", encoding="utf-8") as file:
    lines = file.readlines()
for line in lines:
    if line != "\n" or line != "\r\n":
        merged_corpus.append(line)

with open(inputCorpus3, "r", encoding="utf-8") as file:
    lines = file.readlines()
for line in lines:
    if line != "\n" or line != "\r\n":
        merged_corpus.append(line)

merged_corpus.append("</corpus>")

print("Subcopora merged. Now writing...")

with open("corpus_merged.xml", "w", encoding="utf-8") as file:
    file.write("\n".join(merged_corpus))

print("Done.")