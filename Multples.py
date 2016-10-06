## Multples.py  3 ,5 for Q3 ##

result = 0
for i in range(0, 1000):
    if (i % 3 == 0 or i % 5== 0):
        print i
        result = result + 1
        print result

import unittest

class Mytest(unittest.TestCase):
    def testMultiply(self):
        self.assertEqual((i % 3), 0)
        self.assertEqual((i % 5), 4)

if __name__ == '__main__':
    unittest.main()