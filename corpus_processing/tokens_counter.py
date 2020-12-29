'''
A token counter for corpus files in CWB .vert format. It counts tokens for the whole corpus and for each subcorpus.
'''
from lxml import etree
import re

#set corpus filepath
corpus = r""

token_count_G = 0
token_count_V = 0
token_count_R = 0
token_count_tot = 0

with open(corpus, "r+", encoding="utf-8") as corp:
    parser = etree.XMLParser(encoding='utf-8')
    tree = etree.parse(corp, parser)
    print("Corpus parsed. Now counting tokens...")

    root = tree.getroot()
    s_list_tot = root.findall("text/s")                 # total count
    for s in s_list_tot:
        lines = s.text
        for token in lines.splitlines():
            if token:
                token_count_tot += 1

    s_listG = root.findall("text[@type='Gesetz']/s")   # token count for subcorpora
    for s in s_listG:
        lines = s.text
        for token in lines.splitlines():
            if token:
                token_count_G += 1

    s_listV = root.findall("text[@type='Verwaltungsvorschrift']/s")
    for s in s_listV:
        lines = s.text
        for token in lines.splitlines():
            if token:
                token_count_V += 1

    s_listR = root.findall("text[@type='Gerichtsentscheidung']/s")
    for s in s_listR:
        lines = s.text
        for token in lines.splitlines():
            if token:
                token_count_R += 1


print('Token count of the "gesetze-im-internet.de" subcorpus: %i.' % token_count_G)
print('Token count of the "verwaltungsvorschriften-im-internet.de" subcorpus: %i.' % token_count_V)
print('Token count of the "rechtsprechung-im-internet.de" subcorpus: %i.' % token_count_R)
print("Total token count: %i" % token_count_tot)

