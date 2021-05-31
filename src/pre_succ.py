from src.edgeConverters import *

def v_pre(n: int, m: int, V_dimensions: List[int], H_dimensions: List[int]):
    result = []
    edges = [coordsToNumV(n-1, m, V_dimensions), coordsToNumH(n, m-1, H_dimensions), coordsToNumH(n, m, H_dimensions)]
    for e in edges:
        if e is not None:
            result.append(e)
    return result

def v_succ(n: int, m: int, V_dimensions: List[int], H_dimensions: List[int]):
    result = []
    edges = [coordsToNumV(n+1, m, V_dimensions), coordsToNumH(n+1, m-1, H_dimensions), coordsToNumH(n+1, m, H_dimensions)]
    for e in edges:
        if e is not None:
            result.append(e)
    return result

def h_pre(n: int, m: int, V_dimensions: List[int], H_dimensions: List[int]):
    result = []
    edges = [coordsToNumH(n, m-1, H_dimensions), coordsToNumV(n-1, m, V_dimensions), coordsToNumV(n, m, V_dimensions)]
    for e in edges:
        if e is not None:
            result.append(e)
    return result

def h_succ(n: int, m: int, V_dimensions: List[int], H_dimensions: List[int]):
    result = []
    edges = [coordsToNumH(n, m+1, H_dimensions), coordsToNumV(n-1, m+1, V_dimensions), coordsToNumV(n, m+1, V_dimensions)]
    for e in edges:
        if e is not None:
            result.append(e)
    return result