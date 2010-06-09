all: deps install test

deps: specloud lettuce ludibrio should-dsl
	@python -c 'import pip' 2> /dev/null || easy_install pip

lettuce:
	@python -c 'import lettuce' 2>/dev/null || pip install lettuce

specloud:
	@python -c 'import specloud' 2>/dev/null || pip  install --no-deps specloud -r http://github.com/hugobr/specloud/raw/master/requirements.txt

ludibrio:
	@python -c 'import ludibrio' 2>/dev/null || pip install http://github.com/nsigustavo/ludibrio/tarball/ludibrio3.0

should-dsl:
	@python -c 'import should_dsl' 2>/dev/null || pip install http://github.com/rodrigomanhaes/should-dsl/tarball/matchers-as-functions

install:
	python setup.py install

test: unit functional

unit: specloud ludibrio should-dsl
	@echo =======================================
	@echo  ======== Running SpecLoud ==========
	@specloud specs
	@echo

functional: lettuce
	@echo =======================================
	@echo  ========= Running Lettuce ==========
	@lettuce
	@echo
