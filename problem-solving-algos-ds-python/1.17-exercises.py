class Fraction:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError('Denominator cannot be a value of zero')
        elif type(num) != 'int' or type(den) != 'int':
            raise TypeError('Numerator and Denominator must be integers.')
        else:
            self.num = num
            self.den = den

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den


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
    error = Fraction(1, 0)
    frac3 = frac + frac2
    print(frac3)
    print(frac2 > frac3)
    print(frac2 + frac3)

if __name__ == '__main__':
    main()

