all:
	cythonize -i sin_of_square.pyx
	cythonize -i integrate.pyx
	cythonize -i wave_function.pyx

t:
	python3 test.py

c:
	rm -rf *.so *.cpp *.c