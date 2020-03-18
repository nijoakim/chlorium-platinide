SOURCE=$(wildcard chlorium_platinide/*.py) $(wildcard chlorium_platinide/*/*.py)

.PHONY: all
all: build

.PHONY: clean
clean:
	rm -rf build/

.PHONY: build
build: | build/

.PHONY: run
run: build
	python3 -m chlorium_platinide

.PHONY: install
install: build
	./setup.py install

build/: $(SOURCE)
	mypy --no-color-output --no-implicit-optional -m chlorium_platinide
	./setup.py build
	@touch -c build/
