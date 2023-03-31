#include <iostream>

class SslParams {
public:
    int port;
    bool use_tls;
};

void foo(SslParams& params) {
    std::cout << "port is " << params.port << ", use_tls is " << params.use_tls << std::endl;
}