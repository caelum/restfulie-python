PYTHON=python
PIP=pip
PYTHONPATH := ${PYTHONPATH}:./features/step_definitions
export PYTHONPATH

all: deps install test

deps: specloud lettuce ludibrio should-dsl lxml flask

lettuce:
	@$(PYTHON) -c 'import lettuce' 2>/dev/null || $(PIP) install lettuce

specloud:
	@$(PYTHON) -c 'import specloud' 2>/dev/null || $(PIP) install --no-deps specloud -r http://github.com/hugobr/specloud/raw/master/requirements.txt

ludibrio:
	@$(PYTHON) -c 'import ludibrio' 2>/dev/null || $(PIP) install http://github.com/nsigustavo/ludibrio/tarball/master

should-dsl:
	@$(PYTHON) -c 'import should_dsl' 2>/dev/null || $(PIP) install http://github.com/hugobr/should-dsl/tarball/master

flask:
	@$(PYTHON) -c 'import flask' 2>/dev/null || $(PIP) install flask

lxml:
	@$(PYTHON) -c 'import lxml' 2>/dev/null || $(PIP) install lxml

install:
	$(PYTHON) setup.py install

test: unit functional

unit: specloud ludibrio should-dsl install
	@echo =======================================
	@echo  ======== Running SpecLoud ==========
	@specloud specs
	@echo

functional: lettuce install
	@echo =======================================
	@echo  ========= Running Lettuce ===========
	@lettuce
	@echo

