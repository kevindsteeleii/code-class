class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return '{}/{}'.format(self.num, self.den)

    def __add__(self, other):
        newden = self.den * other.den
        newnum = self.num * other.den + self.den * other.num
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __gt__(self, other):
        return (self.num * other.den) > (other.num * self.den)

def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)



def main():
    frac = Fraction(1,3)
    frac2 = Fraction(2,9)
    print(frac)
    frac3 = frac.add(frac2)
    print(frac3)
    print(frac2 > frac3)
    print(frac2 + frac3)

if __name__ == '__main__':
    main()

