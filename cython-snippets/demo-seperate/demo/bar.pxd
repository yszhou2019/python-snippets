from foo cimport Foo

cdef extern from "bar.h":
    cdef cppclass Bar:
        Bar(Foo&) except +
        void barMethod()

cdef class PyBar:
    cdef Bar* thisptr
    pass