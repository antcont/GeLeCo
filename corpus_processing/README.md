## A set of scripts for corpus processing

Scripts have to be run in the following order:
- `corpus-cleaner_sentence-splitter.py`: removes boilerplate text and marks up sentence boundaries
- `XMLcorpus_merger_tagger.py`: merges subcorpora and adds `<corpus>` tag
- `deduplicate.py`: carries out text deduplication
- `xml2tagged.py`: annotates linguistic mark-up (POS tagging, lemmatisation)
- `tagged2vert.py`: creates the final corpus in word-per-line (WPL) vertical format
- `AddSubcorpus.py`
