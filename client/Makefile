PYTHON=python
PIP=pip
export PYTHONPATH

all: deps install test

deps: specloud ludibrio should-dsl lxml flask

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
	@echo ======================================
	@echo ======== Running unit specs ==========
	@specloud specs
	@echo

functional: specloud should-dsl install
	@echo ==============================================
	@echo ========= Running acceptance specs ===========
	@specloud acceptance
	@echo

