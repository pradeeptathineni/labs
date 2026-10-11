.PHONY: run test check

run:
	./server-stats.sh

test:
	python3 -m unittest discover -s tests -v

check:
	bash -n server-stats.sh
	shellcheck server-stats.sh
	$(MAKE) test
