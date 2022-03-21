'''
Program Input

The first line of the file Prob01.in.txt will contain a positive integer T denoting the number of test cases that follow. Each test case will have the following input:

• A single integer grade, where 0 <= grade <= 100

Example Input:

6
0
48
69
70
87
100

Program Output
For each grade, your program should print PASS is the grade is 70 or above, and FAIL if it is not.

Example Output:

FAIL
FAIL
FAIL
PASS
PASS
PASS
'''

with open ("Prob01.in.txt") as f:
    lines = f.readlines()
    cases = lines.pop(0)

    for line in lines:
        if int(line) < 70:
            print("FAIL")
        else:
            print("PASS")

