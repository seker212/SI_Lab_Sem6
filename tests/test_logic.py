from src.rule_logic_functions import *

def test_2():
    test_object = GlucoseInterface()
    params = [4, 5, 2, 7]
    test_object.solver.add_clause([-5])
    test_object.solver.add_clause([-7])
    test_object.add_exactly_two(params)
    solution = test_object.solve()
    for x in solution.copy():
        if x not in params:
            solution.remove(x)
    assert solution == [2,4]

def test_nq():
    test_object = GlucoseInterface()
    test_object.solver.add_clause([1,2])
    test_object.solver.add_clause([1,3])
    solution = test_object.solve()
    assert solution == [1,-2,-3]
    test_object.add_nq_solution()
    solution = test_object.solve()
    assert solution != [1,-2,-3]
