class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.init(len(edges))
        for e in edges:
            if self.isSame(e[0], e[1]):
                return e
            self.union(e[0], e[1])
        return edges[-1]
    
    def init(self, n):
        self.father = [node for node in range(n + 1)]
        return
    
    def find(self, node):
        if self.father[node] != node:
            self.father[node] = self.find(self.father[node])
        return self.father[node]
    
    def union(self, n1, n2):
        r_n1 = self.find(n1)
        r_n2 = self.find(n2)
        if r_n1 != r_n2:
            self.father[r_n1] = r_n2
        return
    
    def isSame(self, n1, n2):
        r_n1 = self.find(n1)
        r_n2 = self.find(n2)
        return r_n1 == r_n2