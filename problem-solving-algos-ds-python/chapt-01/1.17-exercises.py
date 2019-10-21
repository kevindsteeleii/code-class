class Fraction:
    def __init__(self, num, den):
        if type(num) != int or type(den) != int:
            raise TypeError('Both numerator and denominator need to be integers')
        elif type(den) == int and den == 0:
            raise ValueError('Denominator cannot equal 0. Make it a number more than or less than zero.')
        else:
            den = abs(den)
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

'''
14. Design a class to represent a playing card. Now design a class to represent a deck of cards. Using these two classes, implement a favorite card game.
'''

class Card:
    def __init__(self, suit=None, card=None):
        self.suit = suit
        self.card = card

    def setCard(self, suit, card):
        self.suit = suit
        self.card = card

    def getCard(self):
        return (self.card, self.suit)

    def __str__(self):
        return '{} of {}'.format(self.card, self.suit)

class Deck:
    def __init__(self):
        suits = ['hearts', 'spades', 'clubs', 'diamonds']
        cards = [str(x) for x in range(1, 14)]
        cards[0] = 'Ace'
        cards[10] = 'Jack'
        cards[11] = 'Queen'
        cards[12] = 'King'

        self.all_cards = []
        for suit in suits:
            for card in cards:
                self.all_cards.append(Card(suit, card))

    def deal_card(self):
        return self.all_cards.pop()

    def get_cards(self):
        return self.all_cards

def main():
    c = Card('Hearts', 'Ace')
    d = Deck()
    cards = d.get_cards()
    print(c)

    for item in cards:
        print(item)

if __name__ == '__main__':
    main()

