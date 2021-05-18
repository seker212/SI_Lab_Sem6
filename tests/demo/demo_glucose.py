from pysat.solvers import Glucose3

g = Glucose3()
g.add_clause([1, 2])
g.add_clause([1,3])
g.solve()
print(g.get_model())

