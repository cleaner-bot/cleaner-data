install:
	pip install .

test:
	pytest .

coverage:
	coverage run -m pytest .
	coverage report -m

lint:
	flake8 . --max-line-length 88

test-all: coverage lint
