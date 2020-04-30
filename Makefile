TEST ?=
BLACK_CONFIG ?= --exclude=venv --skip-string-normalization --line-length 100
CHECK ?= --check

.PHONY: run_tests
run_tests:
	python manage.py test ${TEST}

.PHONY: run_tests_local
run_tests_local:
	python manage.py test

check: flake8 black

format: CHECK=
format: black

black:
	black ${BLACK_CONFIG} ${CHECK} .

flake8:
	flake8 .