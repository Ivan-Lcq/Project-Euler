#P21

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore
d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def find_sum_proper_divisor(number):
    sum_proper_divisor=0
    for current_proper_divisor in range(1,number//2+1):
        if number % current_proper_divisor == 0:
            sum_proper_divisor += current_proper_divisor
    return sum_proper_divisor

result=0
for number in range(1,10001):
    op_number=find_sum_proper_divisor(number)
    if op_number == 1 or op_number == number:
        pass
    else:
        op_op_number = find_sum_proper_divisor(op_number)
        if op_op_number == number:
            result += number
print(result)


