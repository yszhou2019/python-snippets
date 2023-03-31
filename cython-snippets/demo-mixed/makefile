# all:
# 	python3 setup.py build_ext --inplace

b:
	python3 setup.py bdist
	cd dist && tar xf *.gz

t:
	python3 test.py

c:
	rm -rf build dist ./demo/foo.cpp