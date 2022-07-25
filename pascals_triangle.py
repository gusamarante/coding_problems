
def pascal(numRows):
    triangle = []

    for i in range(numRows):
        current_line = [1]
        for j in range(i):

            try:
                current_line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            except IndexError:
                current_line.append(1)

        triangle.append(current_line)

    return triangle


print(pascal(5))
