import os, sys

from sympy.abc import T
sys.path.append(os.getcwd())

from typing import List

from src.file_manager import *
from src.edgeConverters import *
from src.rule_logic_functions import *
from src.pre_succ import *

def load(filename):
    # filename = 'matrix.txt'
    pre_val_matrix = GetValuesFromFile(filename)
    val_matrix = Matrix(len(pre_val_matrix), pre_val_matrix[0].count(',')+1)
    SetValuesFromFile(val_matrix, pre_val_matrix)
    return val_matrix

def run(val_matrix):
    V_matrix = Matrix(val_matrix.n, val_matrix.m+1)
    H_matrix = Matrix(val_matrix.n+1, val_matrix.m)
    solver_interface = GlucoseInterface()


    # RULE 1
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

    # RULE 2 - vertical
    for x in range(V_matrix.n):
        for y in range(V_matrix.m):
            solver_interface.add_exactly_one_or_nq_x(coordsToNumV(x,y, [val_matrix.n, val_matrix.m]), v_pre(x, y, [val_matrix.n, val_matrix.m], [val_matrix.n, val_matrix.m]))
            solver_interface.add_exactly_one_or_nq_x(coordsToNumV(x,y, [val_matrix.n, val_matrix.m]), v_succ(x, y, [val_matrix.n, val_matrix.m], [val_matrix.n, val_matrix.m]))

    # RULE 2 - hori
    for x in range(H_matrix.n):
        for y in range(H_matrix.m):
            solver_interface.add_exactly_one_or_nq_x(coordsToNumH(x,y, [val_matrix.n, val_matrix.m]), h_pre(x, y, [val_matrix.n, val_matrix.m], [val_matrix.n, val_matrix.m]))
            solver_interface.add_exactly_one_or_nq_x(coordsToNumH(x,y, [val_matrix.n, val_matrix.m]), h_succ(x, y, [val_matrix.n, val_matrix.m], [val_matrix.n, val_matrix.m]))

    solution = solver_interface.solve()
    # print(solution)
    if solution is None:
        return None
    for x in solution:
        if x > 0 and x % 2 == 0:
            coords = numToCoordsV(x, [val_matrix.n, val_matrix.m])
            if coords is not None:
                V_matrix.SetValue(coords[0], coords[1], True)
        if x < 0 and x % 2 == 0:
            coords = numToCoordsV(-x, [val_matrix.n, val_matrix.m])
            if coords is not None:
                V_matrix.SetValue(coords[0], coords[1], False)
        if x > 0 and x % 2 == 1:
            coords = numToCoordsH(x, [val_matrix.n, val_matrix.m])
            if coords is not None:
                H_matrix.SetValue(coords[0], coords[1], True)
        if x < 0 and x % 2 == 1:
            coords = numToCoordsH(-x, [val_matrix.n, val_matrix.m])
            if coords is not None:
                H_matrix.SetValue(coords[0], coords[1], False)

    while not check_one_loop(V_matrix, H_matrix):
        solver_interface.add_nq_solution()

        solution = solver_interface.solve()
        # print(solution)
        if solution is None:
            return None
        for x in solution:
            if x > 0 and x % 2 == 0:
                coords = numToCoordsV(x, [val_matrix.n, val_matrix.m])
                if coords is not None:
                    V_matrix.SetValue(coords[0], coords[1], True)
            if x < 0 and x % 2 == 0:
                coords = numToCoordsV(-x, [val_matrix.n, val_matrix.m])
                if coords is not None:
                    V_matrix.SetValue(coords[0], coords[1], False)
            if x > 0 and x % 2 == 1:
                coords = numToCoordsH(x, [val_matrix.n, val_matrix.m])
                if coords is not None:
                    H_matrix.SetValue(coords[0], coords[1], True)
            if x < 0 and x % 2 == 1:
                coords = numToCoordsH(-x, [val_matrix.n, val_matrix.m])
                if coords is not None:
                    H_matrix.SetValue(coords[0], coords[1], False)
    return convert_solution(solution, val_matrix)

def convert_solution(solution, val_matrix):  
    if solution is None:
        return None
    coordsV = []
    for x in solution:
        if x > 0 and x % 2 == 0:
            coordsV.append(numToCoordsV(x, [val_matrix.n, val_matrix.m]))

    coordsH = []
    for x in solution:
        if x > 0 and x % 2 == 1:
            coordsH.append(numToCoordsH(x, [val_matrix.n, val_matrix.m]))

    return coordsV, coordsH, solution

def run_none_GUI(filename):
    result = run(load(filename))
    if result is None:
        print("No solution")
    else:
        coordsV, coordsH, solution = result
        print(solution)
        print('')
        for x in coordsV:
            print(x)
        print('---')
        for x in coordsH:
            print(x)
        
# running without GUI - example:
# run_none_GUI("matrix.txt")