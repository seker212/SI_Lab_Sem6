class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[None for count in range(m)] for count in range(n)]
    
    def GetValue(self,x,y):
        return self.matrix[x][y]
    
    def SetValue(self, x, y, value):
        self.matrix[x][y] = value

    def Print(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.GetValue(i,j),end=' ')
            print('')

    
