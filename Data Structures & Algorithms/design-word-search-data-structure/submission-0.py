class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode()
            
            curr = curr.children[word[i]]
        curr.is_end = True
        return

    def search(self, word: str) -> bool:
        return self.helper(self.root, word)
    
    def helper(self, root, word):
        if not word:
            return root.is_end
        
        if word[0] not in root.children and word[0] != '.':
            return False
        
        if word[0] == '.':
            for child in root.children:
                if self.helper(root.children[child], word[1:]):
                    return True
            
            return False
        
        return self.helper(root.children[word[0]], word[1:])