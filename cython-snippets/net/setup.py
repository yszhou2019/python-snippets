from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("net.module1", ["net/module1.pyx"]),
    Extension("net.module2", ["net/module2.pyx"])
]

setup(
    name='net',
    version='1.0',
    packages=['net'],
    ext_modules=cythonize(extensions),
    python_requires='>=3.6',
)