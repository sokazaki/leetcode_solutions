# O(N) Insert/Search/PrefixSearch Time Complexity Solution with Trie

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.isword = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for ch in word:
            cur = cur.nodes[ch]
        cur.isword = True

    def search(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.nodes:
                return False
            cur = cur.nodes[ch]
        return cur.isword

    def startsWith(self, prefix):
        cur = self.root
        for ch in prefix:
            if ch not in cur.nodes:
                return False
            cur = cur.nodes[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
