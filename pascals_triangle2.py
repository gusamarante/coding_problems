"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
Could you optimize your algorithm to use only O(rowIndex) extra space?
"""


def get_row(row_index):
    line = [0 for _ in range(row_index + 1)]
    line[0] = 1
    n = len(line)

    for i in range(1, row_index+1):
        for j in range(i, 0, -1):
            line[j] = line[j] + line[j - 1]

    return line


print(get_row(0))
print(get_row(1))
print(get_row(2))
print(get_row(3))
print(get_row(4))
print(get_row(5))
