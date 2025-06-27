all: results


results: \
	diagrama_H51_08.png


diagrama_H51_08.png:
	./experimentos_TDA_giotto-tda.py

.PHONY: \
	all \
	clean \
	setup

clean:
	rm --force *.png

setup: clean

