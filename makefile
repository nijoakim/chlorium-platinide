PREFIX=/usr/local/bin
SOURCE=$(wildcard platina/*.py) $(wildcard platina/*/*.py) $(wildcard platina/*.c) $(wildcard platina/*/*.c)

all: build

run:
	platina/main.py

clean:
	rm -rf build
	rm -rf platina/*.so

build: $(SOURCE)
	./setup.py build
	touch build
	cp build/*/platina/*.so platina/

install: build
	./setup.py install
