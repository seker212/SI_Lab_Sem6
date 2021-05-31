from threading import setprofile
from pysat.solvers import Glucose3
from typing import List, Optional
from sympy.logic.boolalg import to_cnf
from sympy.abc import A, B, C, D

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
                        q.append(-params[1])
                    else:
                        q.append(params[1])
                elif s == 'B':
                    if t:
                        q.append(-params[2])
                    else:
                        q.append(params[2])
                elif s == 'C':
                    if t:
                        q.append(-params[3])
                    else:
                        q.append(params[3])
                elif s == 'D':
                    if t:
                        q.append(-params[4])
                    else:
                        q.append(params[4])
            self.solver.add_clause(q)

    def add_exactly_three(self, params: List[int]) -> None:
        transformed: List[int] = []
        for p in params:
            transformed.append(-p)
        return self.add_exactly_one(transformed)
    
    def solve():
        self.solver.solve()
        return self.solver.get_model()