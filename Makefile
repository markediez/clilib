TAG := $(shell git rev-parse HEAD)

.PHONY: test
test: build
	docker run -it clilib:$(TAG) bash -cl 'make test-run'

.PHONY: test-run
test-run:
	flake8
	pip install .
	pytest

.PHONY: build
build:
	docker build . -t clilib:$(TAG)
