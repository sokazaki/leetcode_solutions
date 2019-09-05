# O(N) Solution with Simple Approach

import unittest

def fullJustify(words, maxWidth):

    res, wordslist, wordsspace = [], [], 0

    for w in words:
        if wordsspace + len(w) + len(wordslist) > maxWidth:
            for i in range(maxWidth - wordsspace):
                wordslist[i%(len(wordslist)-1 or 1)] += ' '
            res.append(''.join(wordslist))
            wordslist, wordsspace = [], 0
        wordslist += [w]
        wordsspace += len(w)

    return res + [' '.join(wordslist).ljust(maxWidth)]


class Test(unittest.TestCase):

    def test_fullJustify(self):
        self.assertEqual(fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16), ["This    is    an","example  of text","justification.  "])
        self.assertEqual(fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20), ["Science  is  what we","understand      well","enough to explain to","a  computer.  Art is","everything  else  we","do                  "])
        self.assertEqual(fullJustify(["words"], 10), ["words     "])


if __name__ == "__main__":

    unittest.main()
