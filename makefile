PREFIX=/usr/local/bin
SOURCE=$(wildcard platina/*.py) $(wildcard platina/*/*.py)

# TODO: use prefix?

all: build

run:
	scripts/platina

clean:
	rm -rf build

build: $(SOURCE)
	./setup.py build

install: build
	./setup.py install
