from src.edgeConverters import *

def v_pre(n: int, m: int, dimensions: List[int]):
    result = []
    edges = [coordsToNumV(n-1, m, dimensions), coordsToNumH(n, m-1, dimensions), coordsToNumH(n, m, dimensions)]
    for e in edges:
        if e is not None:
            result.append(e)
    return result

def v_succ(n: int, m: int, dimensions: List[int]):
    result = []
    edges = [coordsToNumV(n+1, m, dimensions), coordsToNumH(n+1, m-1, dimensions), coordsToNumH(n+1, m, dimensions)]
    for e in edges:
        if e is not None:
            result.append(e)
    return result

def h_pre(n: int, m: int, dimensions: List[int]):
    result = []
    edges = [coordsToNumH(n, m-1, dimensions), coordsToNumV(n-1, m, dimensions), coordsToNumV(n, m, dimensions)]
    for e in edges:
        if e is not None:
            result.append(e)
    return result

def h_succ(n: int, m: int, dimensions: List[int]):
    result = []
    edges = [coordsToNumH(n, m+1, dimensions), coordsToNumV(n-1, m+1, dimensions), coordsToNumV(n, m+1, dimensions)]
    for e in edges:
        if e is not None:
            result.append(e)
    return result