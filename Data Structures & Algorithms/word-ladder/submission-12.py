class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        self.adjList = {}
        for w in [beginWord] + wordList:
            for i in range(len(w)):
                substr = w[:i] + '*' + w[i + 1:]
                if substr not in self.adjList:
                    self.adjList[substr] = []
                self.adjList[substr].append(w)
        
        visited = {beginWord}
        heap = [(1, beginWord)]
        while heap:
            currLen, currW = heapq.heappop(heap)
            if currW == endWord:
                return currLen
            
            for i in range(len(currW)):
                substr = currW[:i] + '*' + currW[i + 1:]
                for w in self.adjList[substr]:
                    if w not in visited:
                        heapq.heappush(heap, (currLen + 1, w))
                        visited.add(w)
        return 0