#pragma once
#include "foo.h"

class Bar {
public:
    Bar(Foo& foo);
    void barMethod();
private:
    Foo& m_foo;
};