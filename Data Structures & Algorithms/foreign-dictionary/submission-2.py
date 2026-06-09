class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        self.adjList = {char: set() for word in words for char in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    self.adjList[w1[j]].add(w2[j])
                    break
            
        self.result = []
        self.visited = {}
        for char in self.adjList:
            if self.helper(char):
                return ""
        
        self.result.reverse()
        return ''.join(self.result)
    
    def helper(self, c):
        if c in self.visited:
            return self.visited[c]
        
        self.visited[c] = True
        for neighbor in self.adjList[c]:
            if self.helper(neighbor):
                return True
            
        self.visited[c] = False
        self.result.append(c)
        return False