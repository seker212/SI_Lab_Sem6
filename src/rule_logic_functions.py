from pysat.solvers import Glucose3
from typing import List, Optional

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
        for i in range(len(params)-1):
            for j in range(i+1,len(params)):
                for k in range(len(params)):
                    expression: List[int] = 

    def add_exactly_three(self, params: List[int]) -> None:
        transformed: List[int] = []
        for p in params:
            transformed.append(-p)
        return self.add_exactly_one(transformed)