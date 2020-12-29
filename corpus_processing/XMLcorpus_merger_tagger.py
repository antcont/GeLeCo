'''
A script for merging subcorpora and adding the <corpus> root tag.
'''


#set paths for single subcorpora and final merged corpus
subcorpus1 = r""
subcorpus2 = r""
subcorpus3 = r""
merged_corpus_output = r""

merged_corpus = ["<corpus>"]

with open(subcorpus1, "r", encoding="utf-8") as file:
    lines = file.readlines()
for line in lines:
    merged_corpus.append(line)

with open(subcorpus2, "r", encoding="utf-8") as file:
    lines = file.readlines()
for line in lines:
    merged_corpus.append(line)

with open(subcorpus3, "r", encoding="utf-8") as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        merged_corpus.append(line)

merged_corpus.append("</corpus>")

merged_corpus_str = "\n".join(merged_corpus)
print("Subcopora merged. Now writing...")

with open(merged_corpus_output, "w", encoding="utf-8") as file:
    file.write(merged_corpus_str)

print("Done.")