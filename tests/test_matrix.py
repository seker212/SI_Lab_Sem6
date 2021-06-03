from src.matrix import Matrix

def test_a():
    test_mateix = Matrix(3, 5)
    for x in range(test_mateix.n):
        for y in range(test_mateix.m):
            assert test_mateix.matrix[x][y] is None