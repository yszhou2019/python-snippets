# distutils: language = c++
# https://docs.cython.org/en/latest/src/reference/extension_types.html#properties

from cython.operator cimport dereference as deref

cdef extern from "sslparams.h":
    cdef cppclass SslParams:
        int port
        bint use_tls
        SslParams()

cdef extern from "sockclient.h":
    cdef cppclass SockClient:
        SockClient(SslParams& params)
        void send(const char* data, int size)
        void close()

cdef class PySslParams:
    cdef SslParams* thisptr

    def __cinit__(self):
        self.thisptr = new SslParams()
    
    def __dealloc__(self):
        del self.thisptr
    
    # Writable and readable
    property port:

        def __get__(self):
            return deref(self.thisptr).port
        
        def __set__(self, value):
            deref(self.thisptr).port = value
    
    property use_tls:
    
        def __get__(self):
            return deref(self.thisptr).use_tls
        
        def __set__(self, value):
            deref(self.thisptr).use_tls = value
    
    # # Only readable
    # @property
    # def use_tls(self):
    #     return deref(self.thisptr).use_tls
    

cdef class PySockClient:
    cdef SockClient* client

    def __cinit__(self, PySslParams params):
        self.client = new SockClient(deref(params.thisptr))

    def __dealloc__(self):
        del self.client

    def send(self, bytes data):
        self.client.send(data, len(data))

    def close(self):
        self.client.close()

def create_client(PySslParams params):
    return PySockClient(params)
