#P92

"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

result=0

def check_end(number):
    count_89 = 0
    int_number=int(number)
    str_number=str(number)
    while int_number != 89 or int_number != 1:
        new_number = 0
        for th_digit in range(0,len(str_number)):
            square_digit=(int(str_number[th_digit]))**2
            new_number+=square_digit
        int_number=int(new_number)
        str_number=str(new_number)
        if int_number == 89:
            count_89+=1
            break
        elif int_number == 1:
            break
    return count_89

for number in range(1,10000001):
    result+=check_end(number)

print(result)









