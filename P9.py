#P9
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import time

s = time.time()


for a in range(1,1000):
    for b in range(1,1000):
        if a*b==1000*(a+b)-500000:
            c = (a**2+b**2)**0.5
            print('a=',a,' ','b=',b,' ',c)
            print('abc=',a*b*c)

print('TIME : ',time.time() - s,' seconds')



