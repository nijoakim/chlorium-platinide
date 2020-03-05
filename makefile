PREFIX=/usr/local/bin
SOURCE=$(wildcard chlorium-platinide/*.py) $(wildcard chlorium-platinide/*/*.py)

# TODO: use prefix?

.PHONY: all
all: build

.PHONY: clean
clean:
	rm -rf build

.PHONY: build
build: | build/

.PHONY: run
run:
	python3 -m chlorium-platinide

.PHONY: install
install: build
	./setup.py install

build/: $(SOURCE)
	@touch -c build
	./setup.py build
