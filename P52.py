#P52

"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""


for Integer in range(1,1000000):

    Integer_1 = Integer*1
    Integer_2 = Integer*2
    Integer_3 = Integer*3
    Integer_4 = Integer*4
    Integer_5 = Integer*5
    Integer_6 = Integer*6

    Str_Integer_1 = str(Integer_1)
    Str_Integer_2 = str(Integer_2)
    Str_Integer_3 = str(Integer_3)
    Str_Integer_4 = str(Integer_4)
    Str_Integer_5 = str(Integer_5)
    Str_Integer_6 = str(Integer_6)

    Digit_Integer_1 = []
    Digit_Integer_2 = []
    Digit_Integer_3 = []
    Digit_Integer_4 = []
    Digit_Integer_5 = []
    Digit_Integer_6 = []

    for Num_Digit_1 in range(0,len(Str_Integer_1)):
        Digit_Integer_1.append(Str_Integer_1[Num_Digit_1])
    for Num_Digit_2 in range(0,len(Str_Integer_2)):
        Digit_Integer_2.append(Str_Integer_2[Num_Digit_2])
    for Num_Digit_3 in range(0,len(Str_Integer_3)):
        Digit_Integer_3.append(Str_Integer_3[Num_Digit_3])
    for Num_Digit_4 in range(0,len(Str_Integer_4)):
        Digit_Integer_4.append(Str_Integer_4[Num_Digit_4])
    for Num_Digit_5 in range(0,len(Str_Integer_5)):
        Digit_Integer_5.append(Str_Integer_5[Num_Digit_5])
    for Num_Digit_6 in range(0,len(Str_Integer_6)):
        Digit_Integer_6.append(Str_Integer_6[Num_Digit_6])

    if sorted(Digit_Integer_1)==sorted(Digit_Integer_2)==sorted(Digit_Integer_3)==sorted(Digit_Integer_4)==sorted(Digit_Integer_5)==sorted(Digit_Integer_6):
        print(Integer)
        break


