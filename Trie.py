class TrieNode(object):
    def __init__(self) :
        self.children = {}
        self.end = False 
class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for w in word:
            if w not in curr.children :
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return curr.end
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root 
        for w in prefix:
            if w not in curr.children:
                return False 
            curr = curr.children[w]
        return True 
        
