# distutils: language = c++
from foo cimport PyFoo
from bar cimport Bar
from cython.operator cimport dereference as deref

cdef class PyBar:
    def __cinit__(self, PyFoo foo):
        self.thisptr = new Bar(deref(foo.thisptr))

    def __dealloc__(self):
        del self.thisptr

    def barMethod(self):
        return deref(self.thisptr).barMethod()