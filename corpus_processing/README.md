## A set of scripts for corpus processing

- `XMLcorpus_merger_tagger.py`: merges subcorpora and adds `<corpus>` tag
- `corpus-cleaning_sentence-splitting.py`: removes boilerplate text and marks up sentence boundaries
- `deduplicate.py`: carries out text deduplication
- `xml2tagged.py`: annotates linguistic mark-up (POS tagging, lemmatisation), either with SpaCy or TreeTagger
- `tagged2vert.py`: creates the final corpus in word-per-line (WPL) vertical format
- `add_subcorpus.py`: adds a new subcorpus to the master corpus
- `unescape_s.py`: unescapes xml special characters in the final .vert corpus