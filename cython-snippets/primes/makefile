all:
	python3 setup.py build_ext --inplace

t:
	python3 -m timeit -s "from primes_python import primes" "primes(1000)"
	python3 -m timeit -s "from primes_python_compiled import primes" "primes(1000)"
	python3 -m timeit -s "from primes import primes" "primes(1000)"

c:
	rm -rf *.so *.c *.cpp *.html build __pycache__