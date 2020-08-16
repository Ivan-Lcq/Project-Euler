#P4
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
max = 0
for i in range(100,1000):
    for j in range(100,1000):
        palindrome = i*j
        num = str(palindrome)[::-1] #把这个数当字符串反转后相等就是回文
        if (num == str(palindrome)):
            print("回文数",palindrome)
            if palindrome>max:
                max = palindrome;
print("最大是",max)
