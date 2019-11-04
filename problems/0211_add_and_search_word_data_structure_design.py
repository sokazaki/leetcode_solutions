from collections import defaultdict

class WordDictionary(object):
    def __init__(self):
        self.dic = defaultdict(list)

    def addWord(self, word):
        self.dic[len(word)].append(word)

    def search(self, word):
        if '.' not in word:
            return word in self.dic[len(word)]
        else:
            for candidate in self.dic[len(word)]:
                i = 0
                while i < len(candidate):
                    if not (word[i]==candidate[i] or word[i]=='.'):
                        break
                    i += 1
                if i==len(word):
                    return True
            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
