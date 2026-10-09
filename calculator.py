class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def square(self, a):
        return a * a

    def cube(self, a):
        return a * a * a

    def power(self, a, b):
        return a ** b

    def is_even(self, a):
        return a % 2 == 0

    def is_odd(self, a):
        return a % 2 != 0

    def maximum(self, a, b):
        return max(a, b)

    def minimum(self, a, b):
        return min(a, b)