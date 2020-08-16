#P15
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""





i= int(input('number='))
sum1=1
for n in range(1,int((i*2)+1)):
    sum1=sum1*n
sum2=1
for m in range(1,i+1):
    sum2=sum2*m
print(sum1//(sum2*sum2))




