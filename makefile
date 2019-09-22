PREFIX=/usr/local/bin
SOURCE=$(wildcard platina/*.py) $(wildcard platina/*/*.py)

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
	python3 -m platina

.PHONY: install
install: build
	./setup.py install

build/: $(SOURCE)
	@touch -c build
	./setup.py build
