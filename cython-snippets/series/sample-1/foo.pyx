# distutils: language = c++

from libcpp cimport bool as bool_t

cdef extern from "sslparams.h":
    cdef cppclass SslParams:
        int port
        bool_t use_tls

    cdef void foo(SslParams& params)

def call_foo():
    cdef SslParams params
    params.port = 443
    params.use_tls = True
    foo(params)