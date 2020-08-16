#P18

"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)
"""

line1=[75]
line2=[95,64]
line3=[17,47,82]
line4=[18,35,87,10]
line5=[20,4,82,47,65]
line6=[19,1,23,75,3,34]
line7=[88,2,77,73,7,63,67]
line8=[99,65,4,28,6,16,70,92]
line9=[41,41,26,56,83,40,80,70,33]
line10=[41,48,72,33,47,32,37,16,94,29]
line11=[53,71,44,65,25,43,91,52,97,51,14]
line12=[70,11,33,28,77,73,17,78,39,68,17,57]
line13=[91,71,52,38,17,14,91,43,58,50,27,29,48]
line14=[63,66,4,68,89,53,67,30,73,16,69,87,40,31]
line15=[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

#line15
for th_compare in range(0,len(line15)-1):
    compare_element_first = line15[th_compare]
    compare_element_second = line15[th_compare+1]
    if compare_element_first > compare_element_second:
        compare_result = compare_element_first
    elif compare_element_first < compare_element_second:
        compare_result = compare_element_second
    elif compare_element_first == compare_element_second:
        compare_result = compare_element_first
    line14[th_compare] += compare_result

#line14
for th_compare in range(0,len(line14)-1):
    compare_element_first = line14[th_compare]
    compare_element_second = line14[th_compare+1]
    if compare_element_first > compare_element_second:
        compare_result = compare_element_first
    elif compare_element_first < compare_element_second:
        compare_result = compare_element_second
    elif compare_element_first == compare_element_second:
        compare_result = compare_element_first
    line13[th_compare] += compare_result

#line13
for th_compare in range(0,len(line13)-1):
    compare_element_first = line13[th_compare]
    compare_element_second = line13[th_compare+1]
    if compare_element_first > compare_element_second:
        compare_result = compare_element_first
    elif compare_element_first < compare_element_second:
        compare_result = compare_element_second
    elif compare_element_first == compare_element_second:
        compare_result = compare_element_first
    line12[th_compare] += compare_result

#line12
for th_compare in range(0,len(line12)-1):
    compare_element_first = line12[th_compare]
    compare_element_second = line12[th_compare+1]
    if compare_element_first > compare_element_second:
        compare_result = compare_element_first
    elif compare_element_first < compare_element_second:
        compare_result = compare_element_second
    elif compare_element_first == compare_element_second:
        compare_result = compare_element_first
    line11[th_compare] += compare_result

#line11
for th_compare in range(0,len(line11)-1):
    compare_element_first = line11[th_compare]
    compare_element_second = line11[th_compare+1]
    if compare_element_first > compare_element_second:
        compare_result = compare_element_first
    elif compare_element_first < compare_element_second:
        compare_result = compare_element_second
    elif compare_element_first == compare_element_second:
        compare_result = compare_element_first
    line10[th_compare] += compare_result

#line10
for th_compare in range(0,len(line10)-1):
    compare_element_first = line10[th_compare]
    compare_element_second = line10[th_compare+1]
    if compare_element_first > compare_element_second:
        compare_result = compare_element_first
    elif compare_element_first < compare_element_second:
        compare_result = compare_element_second
    elif compare_element_first == compare_element_second:
        compare_result = compare_element_first
    line9[th_compare] += compare_result

#line9
for th_compare in range(0,len(line9)-1):
    compare_element_first = line9[th_compare]
    compare_element_second = line9[th_compare+1]
    if compare_element_first > compare_element_second:
        compare_result = compare_element_first
    elif compare_element_first < compare_element_second:
        compare_result = compare_element_second
    elif compare_element_first == compare_element_second:
        compare_result = compare_element_first
    line8[th_compare] += compare_result

#line8
for th_compare in range(0,len(line8)-1):
    compare_element_first = line8[th_compare]
    compare_element_second = line8[th_compare+1]
    if compare_element_first > compare_element_second:
        compare_result = compare_element_first
    elif compare_element_first < compare_element_second:
        compare_result = compare_element_second
    elif compare_element_first == compare_element_second:
        compare_result = compare_element_first
    line7[th_compare] += compare_result

#line7
for th_compare in range(0,len(line7)-1):
    compare_element_first = line7[th_compare]
    compare_element_second = line7[th_compare+1]
    if compare_element_first > compare_element_second:
        compare_result = compare_element_first
    elif compare_element_first < compare_element_second:
        compare_result = compare_element_second
    elif compare_element_first == compare_element_second:
        compare_result = compare_element_first
    line6[th_compare] += compare_result

#line6
for th_compare in range(0,len(line6)-1):
    compare_element_first = line6[th_compare]
    compare_element_second = line6[th_compare+1]
    if compare_element_first > compare_element_second:
        compare_result = compare_element_first
    elif compare_element_first < compare_element_second:
        compare_result = compare_element_second
    elif compare_element_first == compare_element_second:
        compare_result = compare_element_first
    line5[th_compare] += compare_result

#line5
for th_compare in range(0,len(line5)-1):
    compare_element_first = line5[th_compare]
    compare_element_second = line5[th_compare+1]
    if compare_element_first > compare_element_second:
        compare_result = compare_element_first
    elif compare_element_first < compare_element_second:
        compare_result = compare_element_second
    elif compare_element_first == compare_element_second:
        compare_result = compare_element_first
    line4[th_compare] += compare_result

#line4
for th_compare in range(0,len(line4)-1):
    compare_element_first = line4[th_compare]
    compare_element_second = line4[th_compare+1]
    if compare_element_first > compare_element_second:
        compare_result = compare_element_first
    elif compare_element_first < compare_element_second:
        compare_result = compare_element_second
    elif compare_element_first == compare_element_second:
        compare_result = compare_element_first
    line3[th_compare] += compare_result

#line3
for th_compare in range(0,len(line3)-1):
    compare_element_first = line3[th_compare]
    compare_element_second = line3[th_compare+1]
    if compare_element_first > compare_element_second:
        compare_result = compare_element_first
    elif compare_element_first < compare_element_second:
        compare_result = compare_element_second
    elif compare_element_first == compare_element_second:
        compare_result = compare_element_first
    line2[th_compare] += compare_result

#line2
for th_compare in range(0,len(line2)-1):
    compare_element_first = line2[th_compare]
    compare_element_second = line2[th_compare+1]
    if compare_element_first > compare_element_second:
        compare_result = compare_element_first
    elif compare_element_first < compare_element_second:
        compare_result = compare_element_second
    elif compare_element_first == compare_element_second:
        compare_result = compare_element_first
    line1[th_compare] += compare_result

print(line1)
