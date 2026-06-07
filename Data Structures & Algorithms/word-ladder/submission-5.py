from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        self.adjList = {}
        for word in [beginWord] + wordList:
            for i in range(len(word)):
                substr = word[:i] + '*' + word[i + 1:]
                if substr not in self.adjList:
                    self.adjList[substr] = set()
                self.adjList[substr].add(word)
        
        return self.helper(beginWord, endWord)
    
    def helper(self, start, end):
        q = deque([(start, 0)])
        visited = {start}
        while q:
            curr, currLen = q.popleft()
            if curr == end:
                return currLen + 1

            for i in range(len(curr)):
                substr = curr[:i] + '*' + curr[i + 1:]
                neighbors = self.adjList[substr]
                self.adjList[substr] = []
                for neighbor in neighbors:
                    if neighbor in visited:
                        continue

                    visited.add(neighbor)
                    q.append((neighbor, currLen + 1))
        return 0