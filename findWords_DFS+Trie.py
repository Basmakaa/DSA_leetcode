class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores complete words at the end nodes

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.word = word  # Mark the end of a word

class Solution(object):
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        results = set()

        def dfs(x, y, node):
            if x < 0 or x >= rows or y < 0 or y >= cols or visited[x][y]:
                return
            char = board[x][y]
            if char not in node.children:
                return
            
            visited[x][y] = True
            node = node.children[char]
            if node.word:
                results.add(node.word)
            
            dfs(x - 1, y, node)
            dfs(x + 1, y, node)
            dfs(x, y - 1, node)
            dfs(x, y + 1, node)
            visited[x][y] = False  # Backtrack

        for x in range(rows):
            for y in range(cols):
                dfs(x, y, trie.root)

        return list(results)
