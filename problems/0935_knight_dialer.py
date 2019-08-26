# O(N) Time Complexity / O(1) Space Complexity Solution with Dynamic Programming

import unittest

def knightDialer(N):

    dic = {0:(4,6), 1:(6,8), 2:(7,9), 3:(4,8), 4:(0,3,9), 5:(), 6:(0,1,7), 7:(2,6), 8:(1,3), 9:(2,4)}
    cur = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    for _ in range(N-1):
        prev = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for src_key in range(10):
            for dst_key in dic[src_key]:
                prev[dst_key] = (prev[dst_key]+cur[src_key]) % (10**9+7)
        cur = prev

    return sum(cur) % (10**9+7)


class Test(unittest.TestCase):

    def test_knightDialer(self):
        self.assertEqual(knightDialer(1), 10)
        self.assertEqual(knightDialer(2), 20)
        self.assertEqual(knightDialer(3), 46)
        self.assertEqual(knightDialer(10), 14912)
        self.assertEqual(knightDialer(100), 540641702)
        self.assertEqual(knightDialer(5000), 406880451)

if __name__ == "__main__":

    unittest.main()
