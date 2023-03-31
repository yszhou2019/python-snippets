#include "bar.h"
#include <iostream>

Bar::Bar(Foo& foo) : m_foo(foo) {}

void Bar::barMethod() {
    std::cout << m_foo.x_ + m_foo.y_ << std::endl;
}