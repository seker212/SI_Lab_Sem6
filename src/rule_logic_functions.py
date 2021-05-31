from pysat.solvers import Glucose3
from typing import List, Optional
from sympy.logic.boolalg import to_cnf
from sympy.abc import A, B, C, D

from matrix import Matrix

two_of_four = to_cnf((A&B&~C&~D)|(A&~B&C&~D)|(A&~B&~C&D)|(~A&B&C&~D)|(~A&B&~C&D)|(~A&~B&C&D))

class GlucoseInterface:
    def __init__(self, debug: bool=False) -> None:
        self.solver = Glucose3()
        self._debug: bool = debug

    def add_none_of(self, params: List[int]) -> None:
        for p in params:
            expression: List[int] = [-p]
            self.solver.add_clause(expression)
            if self._debug:
                print(expression)

    def add_exactly_one(self, params: List[int]) -> None:
        # At least one
        expression: List[int] = params
        self.solver.add_clause(expression)
        
        # At most one
        for i in range(len(params)-1):
            for j in range(i+1,len(params)):
                expression: List[int] = [-params[i], -params[j]]
                self.solver.add_clause(expression)
                if self._debug:
                    print(expression)
    
    def add_exactly_two(self, params: List[int]) -> None:
        if len(params) != 4:
            raise NotImplementedError
        for x in two_of_four.args:
            q = []
            for y in x.args:
                t: bool = str(y)[0] == '~'
                s: str = ''
                if t:
                    s = str(y)[1]
                else:
                    s = str(y)[0]
                if s == 'A':
                    if t:
                        q.append(-params[0])
                    else:
                        q.append(params[0])
                elif s == 'B':
                    if t:
                        q.append(-params[1])
                    else:
                        q.append(params[1])
                elif s == 'C':
                    if t:
                        q.append(-params[2])
                    else:
                        q.append(params[2])
                elif s == 'D':
                    if t:
                        q.append(-params[3])
                    else:
                        q.append(params[3])
            self.solver.add_clause(q)

    def add_exactly_three(self, params: List[int]) -> None:
        transformed: List[int] = []
        for p in params:
            transformed.append(-p)
        return self.add_exactly_one(transformed)
    
    def add_nq_solution(self) -> None:
        model: List[int] = self.solver.get_model().copy()
        result: List[int] = []
        for x in model.copy():
            result.append(-x)
        self.solver.add_clause(result)

    def solve(self) -> Optional[List[int]]:
        is_solved = self.solver.solve()
        if is_solved:
            return self.solver.get_model()
        else:
            return None

######

def check_edge(matrix: Matrix, coords: List[int]):
    if coords[0] < 0 or coords[1] < 0:
        return None
    if coords[0] > matrix.n-1 or coords[1] > matrix.m-1:
        return None
    return matrix.GetValue(coords[0], coords[1])

def get_existing_neighbour_edges(verticalMatrix: Matrix, horizontalMatrix: Matrix, coords: List[int], matrixType):
    """Returns coordinates of existing neighbour edges

    Args:
        verticalMatrix (int): [description]
        horizontalMatrix (int): [description]
        coords (List[int]): [description]
        matrixType 9string): [description]

    Returns:
        None: given edge is invalid
        List[int]: list with list of coords from the vertical matrix and list of cords from horizontal matrix
    """
    verticalEdges = []
    horizontalEdges = []

    if matrixType == 'v':
        if check_edge(verticalMatrix, coords) is None: return None

        if check_edge(verticalMatrix, [coords[0]-1, coords[1]]) is not None: verticalEdges.append([coords[0]-1, coords[1]])
        if check_edge(verticalMatrix, [coords[0]+1, coords[1]]) is not None: verticalEdges.append([coords[0]+1, coords[1]])

        if check_edge(horizontalMatrix, [coords[0], coords[1]]) is not None: horizontalEdges.append([coords[0], coords[1]])
        if check_edge(horizontalMatrix, [coords[0], coords[1]-1]) is not None: horizontalEdges.append([coords[0], coords[1]-1])
        if check_edge(horizontalMatrix, [coords[0]+1, coords[1]]) is not None: horizontalEdges.append([coords[0]+1, coords[1]])
        if check_edge(horizontalMatrix, [coords[0]+1, coords[1]-1]) is not None: horizontalEdges.append([coords[0]+1, coords[1]-1])
    else:
        if check_edge(horizontalMatrix, coords) is None: return None

        if check_edge(horizontalMatrix, [coords[0], coords[1]-1]) is not None: horizontalEdges.append([coords[0], coords[1]-1])
        if check_edge(horizontalMatrix, [coords[0], coords[1]+1]) is not None: horizontalEdges.append([coords[0], coords[1]+1])

        if check_edge(verticalMatrix, [coords[0], coords[1]]) is not None: verticalEdges.append([coords[0], coords[1]])
        if check_edge(verticalMatrix, [coords[0], coords[1]+1]) is not None: verticalEdges.append([coords[0], coords[1]+1])
        if check_edge(verticalMatrix, [coords[0]-1, coords[1]]) is not None: verticalEdges.append([coords[0]-1, coords[1]])
        if check_edge(verticalMatrix, [coords[0]-1, coords[1]+1]) is not None: verticalEdges.append([coords[0]-1, coords[1]+1])

    return [verticalEdges, horizontalEdges]

def check_one_loop(verticalMatrix: Matrix, horizontalMatrix: Matrix):
    """Checks if the result contains only one loop

    Args:
        verticalMatrix (int): [description]
        horizontalMatrix (int): [description]

    Returns:
        None: something is wrong
        True: the result contains one loop
        False: the result contains more than one loop or any extra edges
    """

    totalEdgesV = 0
    totalEdgesH = 0
    startEdgeCoords = None
    previousEdgeType = 'v'

    #Firstly, count existing vertical edges and keep the coordinates of the first one
    for i in range (verticalMatrix.n):
        for j in range (verticalMatrix.m):
            if verticalMatrix.GetValue(i,j) is True:
                totalEdgesV += 1
                if startEdgeCoords is None:
                    startEdgeCoords = [i,j]
    if totalEdgesV == 0:
        return None

    #Count existing horizontal edges:
    for i in range (horizontalMatrix.n):
        for j in range (horizontalMatrix.m):
            if horizontalMatrix.GetValue(i,j) is True:
                totalEdgesH += 1
    if totalEdgesH == 0:
        return None

    totalEdges = totalEdgesV+totalEdgesH
    currentEdgeCoords = startEdgeCoords
    previousEdgeCoords = None
    loopEdgeCounter = 0
    newEdgesCords = None

    while (True):
        loopEdgeCounter += 1
        newEdges = get_existing_neighbour_edges(verticalMatrix, horizontalMatrix, currentEdgeCoords, previousEdgeType)
        if len(newEdges[0]+newEdges[1]) != 2:
            return None

        for edge in newEdges[0]:
            if edge != previousEdgeCoords:
                previousEdgeType = 'v'
                newEdgesCords = edge
        for edge in newEdges[1]:
            if edge != previousEdgeCoords:
                previousEdgeType = 'h'
                newEdgesCords = edge

        previousEdgeCoords = currentEdgeCoords
        currentEdgeCoords = newEdgesCords
        if newEdgesCords == startEdgeCoords and previousEdgeType == 'v':
            break

    if loopEdgeCounter == totalEdges:
        return True
    else:
        return False
