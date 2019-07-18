# O(N) Solution with Simple Approach

import unittest

def fizzBuzz(n):
    res = []
    for i in range(1,n+1):
        if i%15==0:
            res.append("FizzBuzz")
        elif i%5==0:
            res.append("Buzz")
        elif i%3==0:
            res.append("Fizz")
        else:
            res.append(str(i))
    return res

class Test(unittest.TestCase):

    def test_fizzBuzz(self):
        self.assertListEqual(fizzBuzz(1), ["1"])
        self.assertListEqual(fizzBuzz(7), ["1","2","Fizz","4","Buzz","Fizz","7"])
        self.assertListEqual(fizzBuzz(16), ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz","16"])

if __name__ == "__main__":

    unittest.main()
