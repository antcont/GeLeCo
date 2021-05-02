## A set of scripts for corpus processing

- `XMLcorpus_merger_tagger.py`: merges the subcorpora
- `corpus-cleaning_sentence-splitting.py`: removes boilerplate text and marks up sentence boundaries. NB: Takes very long when a large list of non-breaking prefixes is provided (> 5000). Reduce the size of that list, if necessary, or use another sentence splitter.
- `deduplicate.py`: carries out text deduplication
- `xml2tagged.py`: annotates linguistic mark-up (POS tagging, lemmatisation). [TreeTagger](https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/) needs to be installed 
- `tagged2vert.py`: creates the final corpus in word-per-line (WPL) vertical format
- `add_subcorpus.py`: adds a new subcorpus to the master corpus
