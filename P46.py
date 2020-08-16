#P46
"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

PrimeL=[]
def Prime_list():
    for i in range(2,17390):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            PrimeL.append(i)
Prime_list()


OddL=[]
def Odd_list():
    num=33
    th=0
    while th<=20000:
        OddL.append(num)
        th += 1
        num += 2
Odd_list()


for odd in OddL:
    for prime in PrimeL:
        if (Sq := (odd - prime)/2) >= 0:
            if (rt := Sq**0.5) % 1 == 0:
                break
        else:
            print(odd)
            break








