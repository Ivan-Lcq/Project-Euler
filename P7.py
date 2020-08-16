#P7
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
i=0
while i<=10000:
    for n in range(2,1000000000000):
        for m in range(2,n):
            if n%m ==0:
                print('not a prime number')
                break

        else:
            i=i+1
            print(i,'th',n)
    break




