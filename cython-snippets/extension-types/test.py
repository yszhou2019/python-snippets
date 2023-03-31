import sin_of_square
import integrate
class MyPolynomial(sin_of_square.Function):
    def evaluate(self, x):
        return 2*x*x + 3*x - 10

integrate.integrate(MyPolynomial(), 0, 1, 10000)