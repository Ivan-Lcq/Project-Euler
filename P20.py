#P20
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

a=1
for i in range(1,101):
    a=a*i
data_0=(f"""{a}""")
data=[]
for n in data_0.split():
    for m in n:
        data.append(int(m))
print(sum(data))



