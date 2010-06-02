all: install test

install:
	python setup.py install

test: unit functional

unit:
	specloud specs

functional:
	lettuce

