# O(N) Solution with Two Pointers

import unittest

def isPalindrome(s):
    i = 0
    j = len(s)-1
    while (i<j):
        if s[i].lower()==s[j].lower():
            i +=1
            j-=1
            continue
        elif not s[i].isalnum():
            i+=1
        elif not s[j].isalnum():
            j-=1
        else:
            return False
    return True


class Test(unittest.TestCase):

    def test_isPalindrome(self):
        self.assertEqual(isPalindrome("A man, a plan, a canal: Panama"), True)
        self.assertEqual(isPalindrome("race a car"), False)
        self.assertEqual(isPalindrome("ab@a"), True)
        self.assertEqual(isPalindrome("a."), True)
        self.assertEqual(isPalindrome("98:7:;7.8-9"), True)
        self.assertEqual(isPalindrome(""), True)

if __name__ == "__main__":

    unittest.main()
