from collections import deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.adjList = {}
        for t in tickets:
            org, dst = t[0], t[1]
            if org not in self.adjList:
                self.adjList[org] = []
            self.adjList[org].append(dst)
        for city in self.adjList:
            self.adjList[city].sort()
        
        return self.helper(len(tickets), "JFK", ["JFK"], set())
        
    def helper(self, numTickets, curr, currPath, used):
        if len(currPath) == numTickets + 1:
            return currPath
        
        if curr not in self.adjList:
            return None

        for i in range(len(self.adjList[curr])):
            if (curr, self.adjList[curr][i], i) in used:
                continue

            currPath.append(self.adjList[curr][i])
            used.add((curr, self.adjList[curr][i], i))
            result = self.helper(numTickets, self.adjList[curr][i], currPath, used)
            if result:
                return result

            currPath.pop()
            used.remove((curr, self.adjList[curr][i], i))
        
        return None