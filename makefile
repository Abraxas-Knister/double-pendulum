.PHONY:
.PHONY: all
all:
	mkdir -p pend
	rm -f pend/*
	python3 data.py
	gnuplot frames
	convert -delay 6 -loop 0 pend/* pendulum.gif

