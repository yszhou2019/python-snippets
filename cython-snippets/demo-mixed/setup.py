from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension('foo',
              sources=['./demo/foo.pyx', './demo/impl_foo.cpp'],
              language='c++'), 
]

setup(
    name='demo',
    version='1.0',
    description='An demo Python C++ extension module',
    ext_modules=cythonize(ext_modules),
)