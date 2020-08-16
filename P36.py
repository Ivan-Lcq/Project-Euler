#P36
"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


sumNum=0



def check_N(num):
    if (str_N_num := str(num)) == (str_N_num_re := str_N_num[::-1]):
        return True



def check_B(num):
    result = ''
    if num == 0:
        result = '0'
    while num > 0:
        result = str(num % 2) + result
        num = num // 2
    if result == (result_re := result[::-1]):
        return True



for num in range(1000000):
    if check_N(num) and check_B(num):
        sumNum=sumNum+num
print(sumNum)







