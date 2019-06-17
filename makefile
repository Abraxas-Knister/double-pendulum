.PHONY:
.PHONY: all
all:
	python3 data.py
	gnuplot frames
	gnuplot energy
	pdflatex energy.tex
