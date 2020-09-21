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

.PHONY: dev
dev:
	docker-compose up -d
	docker-compose exec clilib bash

.PHONY: publish
publish:
	python -m pip install --upgrade setuptools wheel
	python setup.py sdist bdist_wheel
	python -m pip install --upgrade twine
	python -m twine upload --repository pypi dist/*
