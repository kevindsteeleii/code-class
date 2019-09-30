class QuickUnion_UF_Weighted():
    def __init__(self, n):
        '''  
            A weighted version of the QuickUnion_UF class that fashions the root of the smaller tree as sub-tree of the larger to keep the trees from becoming long, skinny ones
            :param n: number, n of objects
        '''
        self.id = list()
        self.sz = list()
        for i in range(n):
            self.id[i] = i
            self.sz[i] = 1

    def __root(self, i):
        weight = 0
        while self.id[i] != i:
            i = self.id[i]
            weight += 1
        self.sz[i] = weight
        return i

    def find(self, p, q):
        return self.__root(p) == self.__root(q)

    def union(self, p, q):
        i , j = self.__root(p), self.__root(q)
        if i == j:
            return
        if (self.sz[i] < self.sz[j]):
            self.id[i] = j
            self.sz[j] += self.sz[j]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        

