#P37
"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

result=0
count=0



def RtL(num):
    strNum=str(num)
    for i in range(len(strNum)):
        for j in range(2,num):
            if num % j == 0:
                break
            elif num == 1:
                break
        else:
            strNum=strNum[0:-1]
            if  strNum== '':
                strNum = '0'
            num = int(strNum)
    if num ==0:
        return True



def LtR(num):
    strNum=str(num)
    for n in range(len(strNum)):
        for m in range(2,num):
            if num % m == 0:
                break
            elif num ==1 :
                break
        else:
            strNum=strNum[1:]
            if strNum == '':
                strNum='0'
            num=int(strNum)
    if strNum == 0:
        return True


for num in range(10,200000):
   if RtL(num) and LtR(num):
        count=count+1
        result=result+num
        print(count,result,num)
















