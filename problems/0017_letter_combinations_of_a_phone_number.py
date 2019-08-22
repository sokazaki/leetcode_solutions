# Simple Solution with Backtracking

import unittest

class Solution:

    def letterCombinations(self, digits):

        if not digits:
            return []

        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        self.dfs(digits, dic, 0, "", res)

        return res

    def dfs(self, digits, dic, idx, s, res):

        if len(s) == len(digits):
            res.append(s)
            return

        for i in range(idx, len(digits)):
            for j in dic[digits[i]]:
                self.dfs(digits, dic, i+1, s+j, res)


class Test(unittest.TestCase):

    def test_letterCombinations(self):
        ans = Solution()
        self.assertEqual(ans.letterCombinations("23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"])
        self.assertEqual(ans.letterCombinations("99"), ["ww","wx","wy","wz","xw","xx","xy","xz","yw","yx","yy","yz","zw","zx","zy","zz"])
        self.assertEqual(ans.letterCombinations("845"), ["tgj","tgk","tgl","thj","thk","thl","tij","tik","til","ugj","ugk","ugl","uhj","uhk","uhl","uij","uik","uil","vgj","vgk","vgl","vhj","vhk","vhl","vij","vik","vil"])
        self.assertEqual(ans.letterCombinations("444"), ["ggg","ggh","ggi","ghg","ghh","ghi","gig","gih","gii","hgg","hgh","hgi","hhg","hhh","hhi","hig","hih","hii","igg","igh","igi","ihg","ihh","ihi","iig","iih","iii"])
        self.assertEqual(ans.letterCombinations("8234"), ["tadg","tadh","tadi","taeg","taeh","taei","tafg","tafh","tafi","tbdg","tbdh","tbdi","tbeg","tbeh","tbei","tbfg","tbfh","tbfi","tcdg","tcdh","tcdi","tceg","tceh","tcei","tcfg","tcfh","tcfi","uadg","uadh","uadi","uaeg","uaeh","uaei","uafg","uafh","uafi","ubdg","ubdh","ubdi","ubeg","ubeh","ubei","ubfg","ubfh","ubfi","ucdg","ucdh","ucdi","uceg","uceh","ucei","ucfg","ucfh","ucfi","vadg","vadh","vadi","vaeg","vaeh","vaei","vafg","vafh","vafi","vbdg","vbdh","vbdi","vbeg","vbeh","vbei","vbfg","vbfh","vbfi","vcdg","vcdh","vcdi","vceg","vceh","vcei","vcfg","vcfh","vcfi"])
        self.assertEqual(ans.letterCombinations(""), [])
        self.assertEqual(ans.letterCombinations("2"), ["a","b","c"])

if __name__ == "__main__":

    unittest.main()
