cdef extern from "foo.h":
    cdef cppclass Foo:
        Foo(int, int) except +
        void fooMethod()
        
    cdef cppclass Bar:
        Bar(Foo&) except +
        void barMethod()