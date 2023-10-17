from math import gcd

class Fraction:
    def __init__(self, a, b):
        GCD = gcd(a, b)
        self.a = a // GCD
        self.b = b // GCD

        if self.b < 0:
            self.a *= -1
            self.b *= -1

    def __str__(self):
        return str(self.a) + "/" + str(self.b)

    def __eq__(self, p):
        return self.a * p.b == p.a * self.b

    def __add__(self, p):
        a = self.a * p.b + p.a * self.b
        b = self.b * p.b
        return Fraction(a, b)

    def __sub__(self, p):
        a = self.a * p.b - p.a * self.b
        b = self.b * p.b
        return Fraction(a, b)

    def __mul__(self, p):
        a = self.a * p.a
        b = self.b * p.b
        return Fraction(a, b)

    def __truediv__(self, p):
        a = self.a * p.b
        b = self.b * p.a
        return Fraction(a, b)

# Do not change the code below this line.
p = Fraction(int(input()), int(input()))
q = Fraction(int(input()), int(input()))
r = Fraction(int(input()), int(input()))
s = (p / q) * (p + q) - q
print(s)
print(s == r)
