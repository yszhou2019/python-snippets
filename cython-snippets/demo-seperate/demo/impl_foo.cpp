#include "foo.h"
#include <iostream>

Foo::Foo(int x, int y) : x_(x), y_(y) {}

void Foo::fooMethod() {
    std::cout << "sum is " << x_ + y_ << std::endl;
}