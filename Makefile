# Makefile for Paladin's Rise EPUB generation

BOOK   = build/paladins-rise.epub
SRC    = $(shell cat filelist.txt) metadata.yml epub.css $(wildcard images/*)

$(BOOK): $(SRC)
	pandoc $$(cat filelist.txt) --metadata-file=metadata.yml \
	       --toc --split-level=1 --css=epub.css \
	       --resource-path=.:images --output=$@

.PHONY: clean
clean:
	rm -rf build

.PHONY: test
test: $(BOOK)
	@echo "EPUB generated successfully: $(BOOK)"
	@ls -lh $(BOOK)

.PHONY: word-count
word-count:
	@if [ -f scripts/wordcount.py ]; then \
		python3 scripts/wordcount.py; \
	else \
		echo "Word count script not found"; \
	fi

.PHONY: master
master:
	python3 scripts/combine_chapters.py

.PHONY: help
help:
	@echo "Available targets:"
	@echo "  $(BOOK)    - Build the EPUB (default)"
	@echo "  clean      - Remove build directory"
	@echo "  test       - Build and verify EPUB"
	@echo "  word-count - Show word count statistics"
	@echo "  master     - Combine all chapters into build/epub-master.md"
	@echo "  help       - Show this help message"
