## Fibonacci.py ##

fib1 =1
fib2 = 2
s = 0

while fib2 <= 4000000:
    s += fib2
    fib1,fib2 = fib1*1+fib2*2,fib1*1+fib2*2
print s

import unittest

class myfib(unittest.TestCase)
    def testfib(selfself):
        self.assertEqual (fib1*1+fib2*2), 23914845)
        self.assertEqual (fib1*1+fib2*3), 31886460)

if __name__ == '_main_':
    unittest.main()