from setuptools import Extension, setup
from Cython.Build import cythonize

ext_modules = cythonize([
    Extension("queue",
              ["queue.pyx"],
              libraries=["calg"])
    ])

setup(ext_modules=ext_modules)