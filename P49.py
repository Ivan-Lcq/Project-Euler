#P49
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

Prime_List=[]

for i in range(1000,10000):
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        Prime_List.append(i)

for element in Prime_List:
    if element+3330 in Prime_List:
        if element+6660 in Prime_List:
            element_1 = element
            element_2 = element+3330
            element_3 = element+6660

            element_1_digit=[]
            element_2_digit=[]
            element_3_digit=[]
            for letter_1 in range(0,len(str(element_1))):
                element_1_digit.append(str(element_1)[letter_1])
            for letter_2 in range(0,len(str(element_2))):
                element_2_digit.append(str(element_2)[letter_2])
            for letter_3 in range(0,len(str(element_3))):
                element_3_digit.append(str(element_3)[letter_3])
            if sorted(element_1_digit) == sorted(element_2_digit) == sorted(element_3_digit):
                print(element_1, element_2, element_3)
                print(str(element_1)+str(element_2)+str(element_3))








