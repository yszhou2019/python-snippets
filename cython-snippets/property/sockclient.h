// sockclient.h
#pragma once
#include "sslparams.h"

class SockClient {
public:
    SockClient(SslParams& params);
    void send(const char* data, int size);
    void close();
};
