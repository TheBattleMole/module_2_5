def get_matrix(n, m, value):
    matrix = []
    matrix_1 = []
    for i in range(1, m+1):
        matrix_1.append(value)
    for j in range(1, n+1):
            matrix.append(matrix_1)
    print(matrix)
get_matrix(1,2,13)
