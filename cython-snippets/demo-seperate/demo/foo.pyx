# distutils: language = c++

from foo cimport Foo
from cython.operator cimport dereference as deref

cdef class PyFoo:
    def __cinit__(self, int x, int y):
        self.thisptr = new Foo(x, y)

    def __dealloc__(self):
        del self.thisptr

    def fooMethod(self):
        return deref(self.thisptr).fooMethod()