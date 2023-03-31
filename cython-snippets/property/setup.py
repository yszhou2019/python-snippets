import os
from distutils.core import setup  
from distutils.extension import Extension  
from Cython.Build import cythonize 

base_path = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.normpath(base_path)
print(base_path)

ext_modules = cythonize([Extension("foo", 
                                   ["foo.pyx"], 
                                   libraries=["sockclient"],
                                   library_dirs=[base_path],
                                   language="c++",
                                   extra_link_args=["-Wl,-rpath,."], # LDFLAGS
                                   )])

setup(
    name='foo',
    ext_modules=ext_modules
)
