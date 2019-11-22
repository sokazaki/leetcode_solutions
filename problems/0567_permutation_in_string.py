# O(N) Solution with Sliding Window + Hashmap

import unittest

def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    cnt_s1 = [0]*26
    cnt_s2 = [0]*26
    for ch in s1:
        cnt_s1[ord(ch)-ord("a")]+=1
    for i, ch in enumerate(s2):
        cnt_s2[ord(ch)-ord("a")]+=1
        if i == len(s1)-1:
            break

    i = 0
    while True:
        if cnt_s1==cnt_s2:
            return True
        if i+len(s1)>=len(s2):
            break
        cnt_s2[ord(s2[i])-ord("a")] -= 1
        cnt_s2[ord(s2[i+len(s1)])-ord("a")] += 1
        i+=1

    return False


class Test(unittest.TestCase):

    def test_checkInclusion(self):
        self.assertEqual(checkInclusion("ab", "eidbaooo"), True)
        self.assertEqual(checkInclusion("ab", "eidboaoo"), False)
        self.assertEqual(checkInclusion("dinitrophenylhydrazine", "acetylphenylhydrazine"), False)
        self.assertEqual(checkInclusion("trinitrophenylmethylnitramine", "dinitrophenylhydrazinetrinitrophenylmethylnitramine"), True)
        self.assertEqual(checkInclusion("hello", "ooolleoooleh"), False)

if __name__ == "__main__":

    unittest.main()
