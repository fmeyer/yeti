PYTHON=python

all: install run_specs

install:
	$(PYTHON) setup.py install

run_specs:
	$(PYTHON) specs/run_all.py
