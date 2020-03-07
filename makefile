SOURCE=$(wildcard chlorium_platinide/*.py) $(wildcard chlorium_platinide/*/*.py)

.PHONY: all
all: build

.PHONY: clean
clean:
	rm -rf build/

.PHONY: build
build: | build/

.PHONY: run
run:
	python3 -m chlorium_platinide

.PHONY: install
install: build
	./setup.py install

build/: $(SOURCE)
	@touch -c build
	./setup.py build
