class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        self.adjList = {}
        for t in tickets:
            if t[0] not in self.adjList:
                self.adjList[t[0]] = []
            self.adjList[t[0]].append(t[1])
        
        self.path = ["JFK"]
        self.helper(len(tickets), "JFK", set())
        return self.path
    
    def helper(self, numTickets, curr, used):
        if len(self.path) == numTickets + 1:
            return True
        
        if curr not in self.adjList:
            return False
        
        for i in range(len(self.adjList[curr])):
            if (curr, self.adjList[curr][i], i) in used:
                continue
            
            self.path.append(self.adjList[curr][i])
            used.add((curr, self.adjList[curr][i], i))
            if self.helper(numTickets, self.adjList[curr][i], used):
                return True
            
            self.path.pop()
            used.remove((curr, self.adjList[curr][i], i))
        
        return False