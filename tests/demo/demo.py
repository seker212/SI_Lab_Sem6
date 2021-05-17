from pysat.formula import CNF
from pysat.solvers import Lingeling

formula = CNF()
formula.append([-1, 2])
formula.append([1, -2])
formula.append([-1, -2])
# formula.append([1, 2])

with Lingeling(bootstrap_with=formula.clauses, with_proof=True) as l:
    if l.solve() == False:
        print(l.get_proof())