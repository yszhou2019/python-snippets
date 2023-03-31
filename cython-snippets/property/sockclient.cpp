// sockclient.cpp
#include "sockclient.h"
#include <iostream>

SockClient::SockClient(SslParams& params) {
    // initialize the socket client with the given SSL parameters
	std::cout << params.port << ", " << params.use_tls << std::endl;
}

void SockClient::send(const char* data, int size) {
    // send the data over the socket
}

void SockClient::close() {
    // close the socket connection
}
