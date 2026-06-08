from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        self.subWMap = {}
        for w in [beginWord] + wordList:
            for i in range(len(w)):
                subW = w[:i] + '*' + w[i + 1:]
                if subW not in self.subWMap:
                    self.subWMap[subW] = []
                self.subWMap[subW].append(w)
        
        return self.helper(beginWord, endWord)
    
    def helper(self, start, end):
        visited = {start}
        q = deque([(start, 1)])
        while q:
            curr, count = q.popleft()
            if curr == end:
                return count
            
            visited.add(curr)
            for i in range(len(curr)):
                subW = curr[:i] + '*' + curr[i + 1:]
                for nextW in self.subWMap[subW]:
                    if nextW in visited:
                        continue
    
                    q.append((nextW, count + 1))
        
        return 0