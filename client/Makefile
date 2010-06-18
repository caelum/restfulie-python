PYTHONPATH := ${PYTHONPATH}:./features/step_definitions
export PYTHONPATH

all: deps install test

deps: specloud freshen ludibrio should-dsl lxml
	@python -c 'import pip' 2> /dev/null || easy_install pip

freshen:
	@python -c 'import freshen' 2>/dev/null || pip install freshen

specloud:
	@python -c 'import specloud' 2>/dev/null || pip  install --no-deps specloud -r http://github.com/hugobr/specloud/raw/master/requirements.txt

ludibrio:
	@python -c 'import ludibrio' 2>/dev/null || pip install http://github.com/nsigustavo/ludibrio/tarball/ludibrio3.0

should-dsl:
	@python -c 'import should_dsl' 2>/dev/null || pip install http://github.com/rodrigomanhaes/should-dsl/tarball/matchers-as-functions

lxml:
	@python -c 'import lxml' 2>/dev/null || pip install lxml

install:
	python setup.py install

test: unit functional

unit: specloud ludibrio should-dsl install
	@echo =======================================
	@echo  ======== Running SpecLoud ==========
	@specloud specs
	@echo

functional: freshen install
	@echo =======================================
	@echo  ========= Running Freshen ===========
	@nosetests --with-freshen -v
	@echo

