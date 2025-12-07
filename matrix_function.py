def multiply(first_matrix, second_matrix):
    if not first_matrix or not second_matrix:
        raise ValueError('Матрицы не должны быть пустыми')

    if len(first_matrix[0]) != len(second_matrix):
        raise ValueError('Количество столбцов первой матрицы должно совпадать с количеством строк второй матрицы')

    rows_first = len(first_matrix)
    columns_first = len(first_matrix[0])
    columns_second = len(second_matrix[0])
    result = [[0 for _ in range(columns_second)] for _ in range(rows_first)]

    for i in range(rows_first):
        for j in range(columns_second):
            for k in range(columns_first):
                result[i][j] += first_matrix[i][k] * second_matrix[k][j]
    return result

def add(first_matrix, second_matrix):
    if not _is_valid_matrix(first_matrix):
        raise ValueError('Первая матрица некорректна: строки имеют разную длину')
    if not _is_valid_matrix(second_matrix):
        raise ValueError('Вторая матрица некорректна: строки имеют разную длину')
    if len(first_matrix) != len(second_matrix) or len(first_matrix[0]) != len(second_matrix[0]):
        raise ValueError('Размерности матриц должны совпадать')
    result = [[0 for _ in range(len(second_matrix[0]))] for _ in range(len(first_matrix))]
    return [[result[i][j] + second_matrix[i][j] for j in range(len(second_matrix[0]))] for i in range(len(first_matrix))]

def _is_valid_matrix(matrix):
    if not matrix or not matrix[0]:
        return True
    row_length = len(matrix[0])
    return all(len(row) == row_length for row in matrix)