class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1  # Store the index of the word in the TrieNode

class WordFilter:
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = TrieNode()
        for index, word in enumerate(words):
            length = len(word)
            # Insert all combinations of suffix#prefix into the Trie
            for i in range(length + 1):
                new_word = word[i:] + '#' + word
                self._insert(new_word, index)

    def _insert(self, word, index):
        """
        Insert the word into the Trie with the associated index.
        """
        current = self.trie
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            current.index = index  # Update the index at every step

    def f(self, pref, suff):
        """
        :type pref: str
        :type suff: str
        :rtype: int
        """
        # Perform a search for suff#pref in the Trie
        current = self.trie
        search_word = suff + '#' + pref
        for char in search_word:
            if char not in current.children:
                return -1  # If the prefix and suffix combination doesn't exist
            current = current.children[char]
        
        return current.index  # Return the latest index found for the combination
