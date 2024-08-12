class TrieNode:
    def __init__(self):
        self.childs = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.childs:
                node.childs[c] = TrieNode()
            node = node.childs[c]
        node.isEnd = True


    def search(self, word: str) -> bool:

        def dfs(word, node, i):
            if i >= len(word):
                return node.isEnd

            if word[i] == ".":
                for c in node.childs:
                    if dfs(word, node.childs[c], i+1):
                        return True
            elif word[i] not in node.childs:
                return False
            else: 
                return dfs(word, node.childs[word[i]], i+1)

        
        return dfs(word, self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
