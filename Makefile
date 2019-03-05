SHELL:=/bin/bash
PROJECT:=gone
all: build test

test:
	( \
		source venv/bin/activate; \
		coverage run --branch --source=${PROJECT} --omit="*test*" -m pytest ${PROJECT}/test/; \
		coverage report; \
	)

build:
	python3.6 -m venv venv
	( \
		source venv/bin/activate; \
		pip install -r requirements.txt; \
		pip install -e .; \
	)

clean:
	rm -rf venv/
	rm -rf .tox/
	rm -rf .mypy_cache/
	rm -rf .pytest_cache/
	rm -rf *.egg-info
	rm -rf .coverage
	find ${PROJECT} -name "__pycache__" -type d -exec rm -rf {} +
