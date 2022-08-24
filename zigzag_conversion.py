"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"


Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
"""


# My own solution
def convert(s, numRows):
    rownidx = []
    zzstr = []
    count = 0
    add = True

    if numRows == 1:
        return s

    for char in s:
        rownidx.append(count)

        if count == 0:
            add = True

        if count == numRows - 1:
            add = False

        if add:
            count += 1
        else:
            count -= 1

    for ri in range(numRows):
        zzstr = zzstr + [char for i, char in zip(rownidx, s) if i == ri]

    zzstr = ''.join(zzstr)

    return zzstr


msg = "AB"
print(convert(msg, 1))
