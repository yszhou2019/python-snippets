from setuptools import setup, Extension
from Cython.Build import cythonize

foo_extension = Extension('foo', ['./demo/foo.pyx'], include_dirs=['./demo'], library_dirs=['./build'], libraries=['foo'], extra_compile_args=['-std=c++11'])
bar_extension = Extension('bar', ['./demo/bar.pyx'], include_dirs=['./demo'], library_dirs=['./build'], libraries=['bar', 'foo'], extra_compile_args=['-std=c++11'])

setup(
    name='demo',
    package_dir={'' : 'demo'},
    ext_modules=cythonize([foo_extension, bar_extension]),
)