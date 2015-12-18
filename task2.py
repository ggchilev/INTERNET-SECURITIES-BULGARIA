def neighbours_sum(m):

    row = 0
    col = 0
    suma = 0
    for j in range(0, len(m) * len(m[0])):
        bomb = m[row][col]
        for item in range(0, len(m)):
            for i in range(0, len(m[0])):
                if (item == row + 1 and (i == col or i == col + 1 or i == col - 1)) or (item == row and (i == col + 1 or i == col - 1)) or (item == row - 1 and (i == col - 1 or i == col or i == col + 1)):
                    suma += m[item][i]
        print('Sum of the neighbours of', m[row][col], 'is', suma)
        suma = 0
        if col != 2:
            col += 1
        else:
            col = 0
            row += 1

neighbours_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
