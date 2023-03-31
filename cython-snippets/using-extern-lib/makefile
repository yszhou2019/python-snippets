all:
# cd c-algorithms && sh autogen.sh && sh configure && make && make install && cd ..
# CFLAGS="-I/usr/local/include/libcalg-1.0" LDFLAGS="-L/usr/local/lib" python3 setup.py build_ext -i
	python3 setup.py build_ext -i

t:
# LD_LIBRARY_PATH="/usr/local/lib:./" python3 test.py
	LD_LIBRARY_PATH="./" python3 test.py

c:
	rm -rf *.so *.cpp *.c build