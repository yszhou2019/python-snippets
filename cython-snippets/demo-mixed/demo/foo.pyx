# distutils: language = c++

from foo cimport Foo
from cython.operator cimport dereference as deref

cdef class PyFoo:
    cdef Foo* thisptr

    def __cinit__(self, int x, int y):
        self.thisptr = new Foo(x, y)

    def __dealloc__(self):
        del self.thisptr

    def fooMethod(self):
        return deref(self.thisptr).fooMethod()

cdef class PyBar:
    cdef Bar* thisptr

    def __cinit__(self, PyFoo foo):
        self.thisptr = new Bar(deref(foo.thisptr))

    def __dealloc__(self):
        del self.thisptr

    def barMethod(self):
        return deref(self.thisptr).barMethod()