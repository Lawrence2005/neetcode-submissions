"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.gMap = {}
        self.cGraph = self.clone(node)
        return self.cGraph
    
    def clone(self, node):
        if not node:
            return None
        
        if node in self.gMap:
            return self.gMap[node]
        
        self.gMap[node] = Node(node.val)
        for n in node.neighbors:
            self.gMap[node].neighbors.append(self.clone(n))
        
        return self.gMap[node]