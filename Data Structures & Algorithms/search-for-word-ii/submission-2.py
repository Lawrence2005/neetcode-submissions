class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.wordTrie = TrieNode()
        self.makeTrie(words, self.wordTrie)

        self.result = set()
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.matchWord(self.wordTrie, board, (i, j), visited, "")
        return list(self.result)
    
    def matchWord(self, node, board, currPos, visited, currWord):
        if board[currPos[0]][currPos[1]] not in node.children:
            return
        
        node = node.children[board[currPos[0]][currPos[1]]]
        currWord += board[currPos[0]][currPos[1]]
        if node.is_end:
            self.result.add(currWord)
        
        visited[currPos[0]][currPos[1]] = True
        for d in self.DIRECTIONS:
            neighbor = (currPos[0] + d[0], currPos[1] + d[1])
            if not (0 <= neighbor[0] < len(board) and 0 <= neighbor[1] < len(board[0])) or visited[neighbor[0]][neighbor[1]]:
                continue
            
            self.matchWord(node, board, neighbor, visited, currWord)
        visited[currPos[0]][currPos[1]] = False

        return

    def makeTrie(self, words, root):
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.is_end = True
        return