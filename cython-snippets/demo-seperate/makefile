b:
	rm -rf build
	mkdir build
	g++ -std=c++11 -fPIC -c -o ./build/foo.o ./demo/impl_foo.cpp -I./demo
	ar rc ./build/libfoo.a ./build/foo.o
	g++ -std=c++11 -fPIC -c -o ./build/bar.o ./demo/impl_bar.cpp -I./demo
	ar rc ./build/libbar.a ./build/bar.o
	python3 setup.py bdist
	cd dist && tar xf *.gz

t:
	python3 test.py

c:
	rm -rf *.cpp build ./demo/*.egg-info dist