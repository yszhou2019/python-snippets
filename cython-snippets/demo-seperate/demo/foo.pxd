cdef extern from "foo.h":
    cdef cppclass Foo:
        Foo(int, int) except +
        void fooMethod()

cdef class PyFoo:
    cdef Foo* thisptr
    pass