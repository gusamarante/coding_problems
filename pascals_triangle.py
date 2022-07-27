
def pascal(numRows):
    triangle = [[1]]

    for i in range(1, numRows):
        current_line = [1]
        for j in range(1, i+1):

            if i >= 1:
                first_term = triangle[i - 1][j - 1]
            else:
                first_term = 0

            try:
                second_term = triangle[i - 1][j]
            except IndexError:
                second_term = 0

            current_line.append(first_term + second_term)

        triangle.append(current_line)

    return triangle


print(pascal(10))
