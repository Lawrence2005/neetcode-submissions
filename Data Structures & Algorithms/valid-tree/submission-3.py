class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        self.adjList = {node: set() for node in range(n)}
        for e in edges:
            self.adjList[e[0]].add(e[1])
            self.adjList[e[1]].add(e[0])
        
        self.visited = set()
        return self.helper(0, -1) and len(self.visited) == n
    
    def helper(self, curr, prev):
        if curr in self.visited:
            return False
        
        self.visited.add(curr)
        for neighbor in self.adjList[curr]:
            if neighbor == prev:
                continue
            
            if not self.helper(neighbor, curr):
                return False
        
        return True