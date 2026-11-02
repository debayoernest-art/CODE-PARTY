def sum_rows(matrix):
    
    result = []
    for row in matrix:
        total = 0
        for number in row:
            total += number
        result.append(total)
    return result


def sum_columns(matrix):
   
    result = []
    for column in range(len(matrix[0])):
        total = 0
        for row in matrix:
            total += row[col]
        result.append(total)
    return result



    matrix = [[2, 3, 4], [1, 5, 7], [4, 6, 8]]

    print(sum_rows(matrix))   
    print(sum_columns(matrix))  



