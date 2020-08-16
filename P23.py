#P23

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
 the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if
this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum
of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can
 be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
  even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is
  less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""


from math import ceil

# Sum of Proper Divisors
def sopd(n):
    if n == 1:
        return 0
    s = 1
    sqrt = ceil(n ** 0.5)
    for b in range(2, sqrt):
        if n % b == 0:
            s += (b + n // b)
    return s + (sqrt if sqrt ** 2 == n else 0)

if __name__ == '__main__':
    abundant = set()
    s = 0
    for i in range(1,28124):
        if not any(i-a in abundant for a in abundant):
            s += i
        if sopd(i) > i:
            abundant.add(i)
    print(s)

