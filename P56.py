#P56

"""
A googol (10**100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?
"""
max_sum=0
for a in range(1,100):
    for b in range(1,100):
        number=a**b
        digits=[]
        str_number=str(number)
        for th_digit in range(0,len(str_number)):
            digits.append(int(str_number[th_digit]))
        current_sum=sum(digits)
        if max_sum < current_sum:
            max_sum=current_sum

print(max_sum)
