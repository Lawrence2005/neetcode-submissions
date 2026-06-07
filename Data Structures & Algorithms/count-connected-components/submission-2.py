class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.init(n)
        for e in edges:
            self.union(e[0], e[1])
        
        count = 0
        for node in range(n):
            if self.find(node) == node:
                count += 1
        return count
    
    def init(self, n):
        self.father = [node for node in range(n)]
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