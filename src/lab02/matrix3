def col_sums(matrix):
    result = []
    max_length_row = max([len(row) for row in matrix])
    try:
        for i in range(max_length_row):
            count = 0
            for row in matrix:
                count += row[i]
            result.append(count)
    except:
        raise ValueError
    return result
matrix = [[1, 2, 3], [4, 5, 6]]
print(col_sums(matrix))