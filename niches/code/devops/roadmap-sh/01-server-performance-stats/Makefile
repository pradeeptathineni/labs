# 01-server-performance-stats/Makefile - Run the report and its checks
# Usage: make run, test, test-linux, or check

# These names are commands rather than files to build
.PHONY: run test test-linux check

# Run the report with its default sample time
run:
	./server-stats.sh

# Run the existing tests on the current host
test:
	python3 -m unittest discover -s tests -v

# Keep the tested Linux setup and leave out the host's other programs
test-linux:
	docker run --rm --network none --read-only \
		--cap-drop ALL --security-opt no-new-privileges \
		--pids-limit 64 --memory 256m --cpus 1 --user 65534:65534 \
		--tmpfs /tmp:rw,nosuid,nodev,exec,size=16m \
		--mount "type=bind,src=$(CURDIR),dst=/lab,readonly" \
		--workdir /lab --entrypoint python3 \
		node@sha256:6dac556d980b7f0e5498d08f08cee0ca67798b4ad6c23964a9214920e67758d0 \
		-B -m unittest discover -s tests -v

# Check shell syntax and style, then run the host tests
check:
	bash -n server-stats.sh
	shellcheck server-stats.sh
	$(MAKE) test
