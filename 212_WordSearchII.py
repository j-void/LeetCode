class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not words or not board:
            return []
        output = set()
        trie = Trie()
        for word in words:
            trie.add_word(word)

        def dfs(i,j, node, word, visited):
            if node.isEnd:
                output.add(word)
                node.isEnd = False

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return
            if (i,j) in visited:
                return
            
            if board[i][j] not in node.children:
                return
            visited.add((i,j))
            dfs(i-1,j,node.children[board[i][j]],word+board[i][j],visited)
            dfs(i+1,j,node.children[board[i][j]],word+board[i][j],visited)
            dfs(i,j-1,node.children[board[i][j]],word+board[i][j],visited)
            dfs(i,j+1,node.children[board[i][j]],word+board[i][j],visited)

            visited.remove((i,j))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,trie.root,"",set())
        
        return list(output)
