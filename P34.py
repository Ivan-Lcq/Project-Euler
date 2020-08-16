#P34

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import time


result=0
s = time.time()

def fact(n):
    if n==1 or n ==0:
        return 1
    else:
        return n*fact(n-1)


def calculate(num):
    sum=0
    strNum=str(num)
    for term in range(1,len(strNum)+1):
        factterm=fact(int(strNum[len(strNum)-term]))
        sum=sum+factterm
    return sum


for num in range(3,100000):
    if calculate(num) == num:
        result=result+num
print('the result is ',result)
print('TIME : ',time.time() - s,' seconds')


























