#pragma once
class Foo {
public:
    int x_;
    int y_;
    Foo(int x, int y);
    void fooMethod();
};


class Bar {
public:
    Bar(Foo& foo);
    void barMethod();
private:
    Foo& m_foo;
};