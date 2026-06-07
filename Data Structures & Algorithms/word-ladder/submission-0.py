from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.adjList, self.shortest = {}, {}
        for word in wordList + [beginWord]:
            self.adjList[word] = []
            self.shortest[word] = float('inf') if word != beginWord else 0
            for other in wordList + [beginWord]:
                if self.wordDist(word, other) != 1:
                    continue
                
                self.adjList[word].append(other)
        if endWord not in self.adjList:
            return 0
        
        self.helper(beginWord, endWord)
        return self.shortest[endWord] + 1 if self.shortest[endWord] != float('inf') else 0
    
    def helper(self, start, end):
        q = deque([(start, 0)])
        while q:
            curr, currLen = q.popleft()
            for neighbor in self.adjList[curr]:
                if currLen + 1 >= self.shortest[neighbor]:
                    continue
                
                self.shortest[neighbor] = currLen + 1
                q.append((neighbor, currLen + 1))
        return

    def wordDist(self, w1, w2):
        distance = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                distance += 1
        return distance