import os, sys
sys.path.append(os.getcwd())

from typing import List

from src.file_manager import *
from src.edgeConverters import *
from src.rule_logic_functions import *
from src.pre_succ import *

if __name__ == '__main__':
    filename = 'matrix.txt'
    pre_val_matrix = GetValuesFromFile(filename)
    val_matrix = Matrix(len(pre_val_matrix), pre_val_matrix[0].count(',')+1)
    SetValuesFromFile(val_matrix, pre_val_matrix)
    V_matrix = Matrix(val_matrix.n+1, val_matrix.m)
    H_matrix = Matrix(val_matrix.n, val_matrix.m+1)
    solver_interface = GlucoseInterface()


    # RULE 1
    for x in range(val_matrix.n):
        for y in range(val_matrix.m):
            params: List[int] = []
            if val_matrix.matrix[x][y] is None:
                continue
            else:
                params.append(coordsToNumH(x,y, [val_matrix.n, val_matrix.m])+25) #FIXME: remove +25
                params.append(coordsToNumH(x+1,y, [val_matrix.n, val_matrix.m])+25) #FIXME: remove +25
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

    # RULE 2 - vertical
    for x in range(V_matrix.n):
        for y in range(V_matrix.m):
            solver_interface.add_exactly_one(v_pre(x, y, [val_matrix.n, val_matrix.m]))
            solver_interface.add_exactly_one(v_succ(x, y, [val_matrix.n, val_matrix.m]))

    # RULE 2 - hori
    for x in range(H_matrix.n):
        for y in range(H_matrix.m):
            solver_interface.add_exactly_one(h_pre(x, y, [val_matrix.n, val_matrix.m]))
            solver_interface.add_exactly_one(h_succ(x, y, [val_matrix.n, val_matrix.m]))

    solution = solver_interface.solve()
    print(solution)
    for x in solution:
        if x > 0 and x <= 25:
            print(numToCoordsV(x, [val_matrix.n, val_matrix.m]))
        if x == 25 or x == -25:
            print('---')
        if x > 25:
            print(numToCoordsH(x, [val_matrix.n, val_matrix.m]))