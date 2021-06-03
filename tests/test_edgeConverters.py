from src.edgeConverters import *
from src.matrix import *

def test_a():
    matrix = Matrix(3, 6)
    V_matrix = Matrix(matrix.n, matrix.m+1)
    H_matrix = Matrix(matrix.n+1, matrix.m)
    before = []

    for x in range(V_matrix.n):
        for y in range(V_matrix.m):
            num = coordsToNumV(x, y, [matrix.n, matrix.m])
            assert before.count(num) == 0
            before.append(num)
            assert numToCoordsV(num, [matrix.n, matrix.m]) == (x, y)

    assert len(before) == V_matrix.n * V_matrix.m

    for x in range(H_matrix.n):
        for y in range(H_matrix.m):
            num = coordsToNumH(x, y, [matrix.n, matrix.m])
            assert before.count(num) == 0
            before.append(num)
            assert numToCoordsH(num, [matrix.n, matrix.m]) == (x, y)

    assert len(before) == V_matrix.n * V_matrix.m + H_matrix.n * H_matrix.m 
    for x in range(1, V_matrix.n * V_matrix.m + H_matrix.n * H_matrix.m + 1):
        assert x in before