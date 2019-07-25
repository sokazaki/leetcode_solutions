# Solution with simple approach

import unittest

def numUniqueEmails(emails):
    res = set()
    for email in emails:
        local, domain = email.split('@')
        local = local.split('+')[0].replace('.', '')
        res.add((local, domain))
    return len(res)


class Test(unittest.TestCase):

    def test_numUniqueEmails(self):
        self.assertEqual(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]), 2)
        self.assertEqual(numUniqueEmails(["test.emailalex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]), 3)
        self.assertEqual(numUniqueEmails([]), 0)

if __name__ == "__main__":

    unittest.main()
