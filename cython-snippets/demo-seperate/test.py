from foo import PyFoo
from bar import PyBar

a = PyFoo(1, 2)
b = PyBar(a)
a.fooMethod()
b.barMethod()