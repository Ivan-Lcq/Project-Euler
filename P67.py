#P67

"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in P67_text.txt (right click and 'Save Link/Target As...'),
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try
every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012)
routes every second it would take over twenty billion years to check them all. There is an efficient
algorithm to solve it. ;o)
"""

f=open(r'P67_text.txt')
line_total=[]
for i in range(100):
    line_total.append([])
    x=f.readline()
    for j in range(100):
        try:
            line_total[i].append(int(x[j*3:(j*3)+2]))
        except ValueError:
            pass
f.close()

line_total = line_total[::-1]

for th_line_compare in range(0,len(line_total)-1):
    compare_line_first = line_total[th_line_compare]
    compare_line_second = line_total[th_line_compare+1]
    for th_element_compare in range(0,len(compare_line_first)-1):
        compare_element_first = compare_line_first[th_element_compare]
        compare_element_second = compare_line_first[th_element_compare+1]
        if compare_element_first > compare_element_second:
            compare_result = compare_element_first
        elif compare_element_first < compare_element_second:
            compare_result = compare_element_second
        elif compare_element_first == compare_element_second:
            compare_result = compare_element_first
        compare_line_second[th_element_compare] += compare_result
    line_total[th_line_compare+1] = compare_line_second
print(line_total[-1])





