''' 
    A class made to represent the Union-Find DS that implements quick find/slow union algorithm
'''
class QuickFind_UF():
    def __init__(self, n):
        ''' 
        :param n: the number of nodes/objects to possibly be in a union/connected
        :type n: int
        :return: new instance of QuickFind_UF class
        '''
        self.id = list()
        for i in range(len(n)):
            self.id.append(i)

    def find(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        '''  
        :param p: first object to be connected to the second
        :param q: second object
        :return None:\n
        as the name suggests, if finds out if objects are connected but is potentionally quadratic in time of execution
        '''
        p_id = self.id[p]
        q_id = self.id[q]
        for i in range(len(self.id)):
            if (self.id[i] == p_id):
                self.id[i] = q_id