from src.rule_logic_functions import *
from src.matrix import *

def test_0():
    test_object = GlucoseInterface()
    params = [4, 5, 2]
    test_object.solver.add_clause([-1, 3])
    test_object.solver.add_clause([1, -5])
    test_object.add_none_of(params)
    
    counter = 0
    solution = test_object.solve()
    while solution is not None:
        print(f'Solution: {solution}')
        counter += 1
        test_object.add_nq_solution()
        solution = test_object.solve()
    assert counter == 3

def test_2():
    test_object = GlucoseInterface()
    params = [4, 5, 2, 3]
    test_object.solver.add_clause([-5])
    test_object.solver.add_clause([1, -2])
    test_object.add_exactly_two(params)
    
    counter = 0
    solution = test_object.solve()
    while solution is not None:
        print(f'Solution: {solution}')
        counter += 1
        test_object.add_nq_solution()
        solution = test_object.solve()
    assert counter == 4

def test_nq():
    test_object = GlucoseInterface(debug=True)
    test_object.solver.add_clause([1,2])
    test_object.solver.add_clause([-1,3])

    counter = 0
    solution = test_object.solve()
    while solution is not None:
        print(f'Solution: {solution}')
        counter += 1
        test_object.add_nq_solution()
        solution = test_object.solve()
    assert counter == 4
