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
	docker-compose up
	docker-compose exec clilib bash

.PHONY: publish
publish:
	python -m pip install --user --upgrade setuptools wheel
	python setup.py sdist bdist_wheel
	python3 -m pip install --user --upgrade twine
	python3 -m twine upload --repository clilib dist/*