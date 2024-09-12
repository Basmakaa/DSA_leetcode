class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.end = True  # Mark the end of the word

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def search_node(word, node):
            if not word:
                return node.end
            
            first = word[0]
            rest = word[1:]

            if first == ".":
                # Check all children of the current node
                for child in node.children.values():
                    if search_node(rest, child):
                        return True
                return False
            else:
                if first not in node.children:
                    return False
                return search_node(rest, node.children[first])
        
        return search_node(word, self.root)
