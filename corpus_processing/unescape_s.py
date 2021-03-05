'''
Final unescaping of text contained in <s> tags. ALso removing any remaining empty lines.
'''
from xml.sax.saxutils import unescape
import gc
from yaspin import yaspin

gc.set_threshold(1000, 15, 15)      # setting higher tresholds for garbage collection, in order to avoid memory peaks

input_corpus = r"C:\Users\anton\PycharmProjects\GeLeCo\GVR_merged_sentence-splitted_treetagged_ded_trim_vert.xml"
output_corpus = r"C:\Users\anton\PycharmProjects\GeLeCo\GVR_merged_sentence-splitted_treetagged_ded_trim_vert_unescaped.xml"

with open(input_corpus, "r+", encoding="utf-8") as file:
    lines = file.readlines()
    print("corpus parsed")

with open(output_corpus, "w+", encoding="utf-8") as corpus:
    with yaspin().bold.cyan.aesthetic as sp:  # printing spinner and % progress
        counter = 0
        empty = 0
        for line in lines:
            if not line.startswith("<"):
                line = unescape(line)
                line = line.replace("&quot;", "\"")
            if line == "\n" or line == "\r\n":
                print("empty line found")
                empty += 1
                continue
            corpus.write(line)
            counter += 1
            if (counter / 100000).is_integer():  # refresh counter each 100000 lines
                sp.text = "%i lines written" % counter

print("Empty lines found and discarded: ", empty)
print("Done")