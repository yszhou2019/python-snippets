b:
	g++ -std=c++17 -fPIC -shared -o libsockclient.so sockclient.cpp
	python3 setup.py build_ext --inplace

t:
	python3 test.py

c:
	rm -rf *.so foo.cpp build
