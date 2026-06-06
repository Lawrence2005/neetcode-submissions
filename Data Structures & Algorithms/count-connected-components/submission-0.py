class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        
        self.adjList = {node: set() for node in range(n)}
        for e in edges:
            self.adjList[e[0]].add(e[1])
            self.adjList[e[1]].add(e[0])
        
        count = 0
        self.toVisit = {node for node in range(n)}
        while self.toVisit:
            for node in range(n):
                if node not in self.toVisit:
                    continue

                count += 1
                self.helper(node)
        
        return count

    def helper(self, node):
        self.toVisit.remove(node)
        for neighbor in self.adjList[node]:
            if neighbor not in self.toVisit:
                continue
                
            self.helper(neighbor)
        return