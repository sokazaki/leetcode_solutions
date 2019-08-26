# Simple Solution with Recursion

import unittest

def numberToWords(num):

    dic1 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    dic2 = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def words(n):
        if n < 20:
            return dic1[n-1:n]
        if n < 100:
            return [dic2[n//10-2]] + words(n%10)
        if n < 1000:
            return [dic1[n//100-1]] + ['Hundred'] + words(n%100)
        if n < 1000**2:
            return words(n//1000) + ['Thousand'] + words(n%1000)
        if n < 1000**3:
            return words(n//1000**2) + ['Million'] + words(n%1000**2)
        if n < 1000**4:
            return words(n//1000**3) + ['Billion'] + words(n%1000**3)

    return ' '.join(words(num)) or 'Zero'


class Test(unittest.TestCase):

    def test_numberToWords(self):
        self.assertEqual(numberToWords(0), "Zero")
        self.assertEqual(numberToWords(123), "One Hundred Twenty Three")
        self.assertEqual(numberToWords(123000), "One Hundred Twenty Three Thousand")
        self.assertEqual(numberToWords(1000010), "One Million Ten")
        self.assertEqual(numberToWords(12345), "Twelve Thousand Three Hundred Forty Five")
        self.assertEqual(numberToWords(1234567), "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")
        self.assertEqual(numberToWords(1234567891), "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One")


if __name__ == "__main__":

    unittest.main()
