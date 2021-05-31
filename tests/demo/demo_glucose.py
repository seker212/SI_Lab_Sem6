from pysat.solvers import Glucose3

g = Glucose3()
g.add_clause([4, 2])
g.add_clause([4,34])
g.solve()
print(g.get_model())

