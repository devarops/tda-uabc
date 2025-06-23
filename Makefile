all: results


results: \
	reports/figures/diagrama_0A7_01.png \
	reports/figures/diagrama_H51_08.png \
	reports/figures/diagrama_H52_07.png


reports/figures/diagrama_0A7_01.png:
	$(checkDirectories)
	python experimentos_TDA_giotto-tda.py --input trip_0A7_01.csv --output diagrama_0A7_01.png

reports/figures/diagrama_H51_08.png:
	$(checkDirectories)
	python experimentos_TDA_giotto-tda.py --input trip_H51_08.csv --output diagrama_H51_08.png

reports/figures/diagrama_H52_07.png:
	$(checkDirectories)
	python experimentos_TDA_giotto-tda.py --input trip_H52_07.csv --output diagrama_H52_07.png


define renderLatex
	cd $(<D) && pdflatex $(<F)
	cd $(<D) && pdflatex $(<F)
endef

define checkDirectories
	mkdir --parents $(@D)
endef


.PHONY: \
	all \
	clean \
	setup

clean:
	rm --force --recursive reports
	rm --force --recursive data
	rm --force *.pdf

setup: clean

