class Fraction:
    def __init__(self, num, den):
        if type(num) != int or type(den) != int:
            raise TypeError('Both numerator and denominator need to be integers')
        elif type(den) == int and den == 0:
            raise ValueError('Denominator cannot equal 0. Make it a number more than or less than zero.')
        else:
            _gcd = gcd(num, den)
            self.num = num//_gcd
            self.den = den//_gcd

    def __str__(self):
        return '{}/{}'.format(self.num, self.den)

    def __add__(self, other):
        newden = self.den * other.den
        newnum = self.num * other.den + self.den * other.num
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __sub__(self, other):
        newden = self.den * other.den
        newnum = self.num * other.den - self.den * other.num
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __gt__(self, other):
        return (self.num * other.den) > (other.num * self.den)

    def __lt__(self, other):
        return (self.num * other.den) < (other.num * self.den)

    def __le__(self, other):
        return (self.num * other.den) <= (other.num * self.den)

    def __ge__(self, other):
        return (self.num * other.den) >= (other.num * self.den)

    def __eq__(self, other):
        return (self.num * other.den) == (other.num * self.den)

    def __ne__(self, other):
        return (self.num * other.den) != (other.num * self.den)

    def __mul__(self, other):
        newNum = self.num * other.num
        newDen = self.den * other.den
        _gcd = gcd(newNum, newDen)
        return Fraction(newNum//_gcd, newDen//_gcd)

    def __truediv__(self, other):
        newNum = self.num * other.den
        newDen = self.den * other.num
        _gcd = gcd(newNum, newDen)
        return (newNum//_gcd) / (newDen//_gcd)


def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


def main():
    frac = Fraction(1,3)
    frac2 = Fraction(2,9)
    print(frac)
    frac3 = frac + frac2
    frac4 = Fraction(5, 9)

    print(frac4 >= frac3)
    frac5 = frac4 * frac2
    print(frac5)
    frac6 = frac4 / frac2
    print(frac6)

if __name__ == '__main__':
    main()

