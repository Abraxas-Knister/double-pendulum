.PHONY:
.PHONY: all
all:
	mkdir -p pend
	rm -f pend/*
	python3 data.py
	gnuplot frames
	gnuplot energy
	convert -delay 6 -loop 0 pend/* pendulum.gif

