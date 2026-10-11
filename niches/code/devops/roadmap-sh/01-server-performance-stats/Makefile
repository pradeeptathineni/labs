.PHONY: run test test-linux check

run:
	./server-stats.sh

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

check:
	bash -n server-stats.sh
	shellcheck server-stats.sh
	$(MAKE) test
