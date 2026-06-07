from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.adjList = {}
        for word in wordList + [beginWord]:
            self.adjList[word] = []
            for other in wordList + [beginWord]:
                if self.wordDist(word, other) != 1:
                    continue
                
                self.adjList[word].append(other)
        if endWord not in self.adjList:
            return 0
        
        return self.helper(beginWord, endWord, set())
    
    def helper(self, start, end, visited):
        q = deque([(start, 0)])
        visited.add(start)
        while q:
            curr, currLen = q.popleft()
            if curr == end:
                return currLen + 1
                
            for neighbor in self.adjList[curr]:
                if neighbor in visited:
                    continue

                visited.add(neighbor)
                q.append((neighbor, currLen + 1))
        return 0

    def wordDist(self, w1, w2):
        distance = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                distance += 1
        return distance