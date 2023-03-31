#include "foo.h"
#include <iostream>

Foo::Foo(int x, int y) : x_(x), y_(y) {}

void Foo::fooMethod() {
    std::cout << "sum is " << x_ + y_ << std::endl;
}

Bar::Bar(Foo& foo) : m_foo(foo) {}

void Bar::barMethod() {
    std::cout << m_foo.x_ + m_foo.y_ << std::endl;
}