
.PHONY: test
test:
	flake8
	pip install .
	pytest
