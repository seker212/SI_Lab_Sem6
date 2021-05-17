class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[None for count in range(n)] for count in range(m)]
    
    def GetValue(self,x,y):
        return self.matrix[x][y]
    
    def SetValue(self, x, y, value):
        self.matrix[x][y] = value

    
