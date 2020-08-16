#P31
"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
import time
s = time.time()

answer=[1]+[0]*200
data=[1,2,5,10,20,50,100,200]
for i in data:
    for j in range(i,201):
        answer[j]+=answer[j-i]
print(answer[200])
print('TIME : ',time.time() - s,' seconds')
