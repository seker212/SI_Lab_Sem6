import os, sys
sys.path.append(os.getcwd())

from typing import List

from src.file_manager import *
from src.edgeConverters import *
from src.rule_logic_functions import *

if __name__ == '__main__':
    filename = 'matrix.txt'
    pre_val_matrix = GetValuesFromFile(filename)
    val_matrix = Matrix(pre_val_matrix[0].count(',')+1, len(pre_val_matrix))
    SetValuesFromFile(val_matrix, pre_val_matrix)
    V_matrix = Matrix(val_matrix.n+1, val_matrix.m)
    H_matrix = Matrix(val_matrix.n, val_matrix.m+1)
    solver_interface = GlucoseInterface()

    for x in range(val_matrix.n):
        for y in range(val_matrix.m):
            params: List[int] = []
            if val_matrix.matrix[x][y] is None:
                continue
            else:
                params.append(coordsToNumH(x,y, [val_matrix.n, val_matrix.m]))
                params.append(coordsToNumH(x+1,y, [val_matrix.n, val_matrix.m]))
                params.append(coordsToNumV(x,y, [val_matrix.n, val_matrix.m]))
                params.append(coordsToNumV(x,y+1, [val_matrix.n, val_matrix.m]))

            if val_matrix.matrix[x][y] == 0:
                solver_interface.add_none_of(params)
            elif val_matrix.matrix[x][y] == 1:
                solver_interface.add_exactly_one(params)
            elif val_matrix.matrix[x][y] == 2:
                solver_interface.add_exactly_two(params)
            elif val_matrix.matrix[x][y] == 3:
                solver_interface.add_exactly_three(params)
    print(solver_interface.solve())