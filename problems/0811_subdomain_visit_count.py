# O(N) Solution with Hash Map

import unittest

def subdomainVisits(cpdomains):
    dic = {}
    for cpdomain in cpdomains:
        num, domain = cpdomain.split(" ")
        domains = domain.split('.')
        for idx in range(len(domains)):
            subdomain = '.'.join(domains[idx:])
            val = dic.get(subdomain, 0)
            val += int(num)
            dic[subdomain] = val

    res = []
    for subdomain, count in dic.items():
        res.append(" ".join([str(count), subdomain]))

    return res


class Test(unittest.TestCase):

    def test_subdomainVisits(self):
        self.assertCountEqual(subdomainVisits(["9001 discuss.leetcode.com"]), ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"])
        self.assertCountEqual(subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]), ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"])
        self.assertCountEqual(subdomainVisits(["1 discuss.leetcode.com", "1 leetcode.com", "1 codeforces.com", "1 atcoder.jp"]), ["1 atcoder.jp","1 discuss.leetcode.com","1 codeforces.com","3 com","1 jp","2 leetcode.com"])
        self.assertCountEqual(subdomainVisits(["1 atcoder.jp"]), ["1 atcoder.jp","1 jp"])

if __name__ == "__main__":

    unittest.main()
