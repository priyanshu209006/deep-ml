def matrixmul(a: list[list[int | float]],
              b: list[list[int | float]]) -> list[list[int | float]]:

    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])

    if cols_a != rows_b:
        return -1
    c = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for x in range(rows_a):
        for i in range(cols_b):
            for j in range(cols_a):
                c[x][i] += a[x][j] * b[j][i]

    return c