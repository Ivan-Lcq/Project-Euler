#P16
"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""


data_0=str(2**1000)

data = []
for a in data_0.split():
    for b in a :
        data.append(int(b))


print(sum(data))
