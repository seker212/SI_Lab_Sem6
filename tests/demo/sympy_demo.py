from sympy.logic.boolalg import to_cnf
from sympy.abc import A, B, C, D
from pysat.solvers import Glucose3

g = Glucose3()
a = to_cnf((A&B&~C&~D)|(A&~B&C&~D)|(A&~B&~C&D)|(~A&B&C&~D)|(~A&B&~C&D)|(~A&~B&C&D))
b = 3
with open('test.txt', 'w') as ff:
    ff.write(str(a))
with open('test2.txt', 'w') as fff:
    for x in a.args:
        print(x)
        fff.write(str(x)+'\n')
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
                    q.append(-1)
                else:
                    q.append(1)
            elif s == 'B':
                if t:
                    q.append(-2)
                else:
                    q.append(2)
            elif s == 'C':
                if t:
                    q.append(-3)
                else:
                    q.append(3)
            elif s == 'D':
                if t:
                    q.append(-4)
                else:
                    q.append(4)
        print(q)
        g.add_clause(q)
        fff.write(str(q)+'\n')
g.add_clause([-1])
g.add_clause([-3])
g.add_clause([-2])
g.solve()
print(g.get_model())