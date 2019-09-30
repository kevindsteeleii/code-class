
class QuickUnion_UF():
    def __init__(self, n):
        '''  
        The python3 implementation of the QuickUnion_UF class
        :param n: number of items total, n - 1
        '''
        self.id = list()
        for i in range(n):
            self.id.append(i)

    def __root(self, i):
        ''' 
        A "private" method that takes an object and seeks the root of its tree 
        :param i: object whose root has to be sought out
        '''
        while i != self.id[i]:
            i = self.id[i]
        return i

    def find(self, p, q):
        return self.__root(p) == self.__root(q)

    def union(self, p, q):
        self.id[self.__root(p)] = self.__root(q)

        