PYTHON=python
EASY_INSTALL=easy_install
PIP=pip
PYTHONPATH := ${PYTHONPATH}:./features/step_definitions
export PYTHONPATH

all: easy_install pip deps install test

easy_install:
	if ! [ -e "ez_setup.py" ]; then	 wget http://peak.telecommunity.com/dist/ez_setup.py;	$(PYTHON) setup.py install ;fi

pip:
	@$(PYTHON) -c 'import pip' 2> /dev/null || $(EASY_INSTALL) pip

deps: specloud lettuce ludibrio should-dsl lxml

lettuce:
	@$(PYTHON) -c 'import lettuce' 2>/dev/null || $(PIP) install lettuce

specloud:
	@$(PYTHON) -c 'import specloud' 2>/dev/null || $(PIP) install --no-deps specloud -r http://github.com/hugobr/specloud/raw/master/requirements.txt

ludibrio:
	@$(PYTHON) -c 'import ludibrio' 2>/dev/null || $(PIP) install http://github.com/nsigustavo/ludibrio/tarball/master

should-dsl:
	@$(PYTHON) -c 'import should_dsl' 2>/dev/null || $(PIP) install http://github.com/hugobr/should-dsl/tarball/master

lxml:
	@$(PYTHON) -c 'import lxml' 2>/dev/null || $(PIP) install lxml && sudo apt-get install libxml2 libxslt1.1 libxslt-dev

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

