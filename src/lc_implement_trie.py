class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        n = self.root
        for c in word:
            if c not in n:
                n[c] = dict()
            n = n[c]
        n[""] = 1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        n = self.root
        for c in word:
            if c not in n:
                return False
            n = n[c]
        return "" in n

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        n = self.root
        for c in prefix:
            if c not in n:
                return False
            n = n[c]
        return True


def test_trie():
    trie = Trie()

    trie.insert("apple")
    assert trie.search("apple")
    assert trie.search("app") is False
    assert trie.startsWith("app")
    trie.insert("app")
    assert trie.search("app")
