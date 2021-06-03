from typing import List

def coordsToNumV(row: int, col: int, dimensions: List[int]):
    """Converts vertical edge co-ordinates to its number.
    Vertical edges are represented as even numbers.

    Args:
        row (int): [description]
        col (int): [description]
        dimensions (List[int]): [description]

    Returns:
        Optional[int]: [description]
    """

    if row >= dimensions[0] or col > dimensions[1] or row < 0 or col < 0:
        return None
    return (col * dimensions[0] + row+1) * 2

def coordsToNumH(row: int, col: int, dimensions: List[int]):
    """ Converts horizontal edge co-ordinates to its number.
    Horizontal edges are represented as odd numbers.

    Args:
        row (int): [description]
        col (int): [description]
        dimensions (List[int]): [description]

    Returns:
        Optional[int]: [description]
    """
    if row > dimensions[0] or col >= dimensions[1] or row < 0 or col < 0:
        return None
    return (row * dimensions[1] + col+1) * 2 - 1

def numToCoordsV(num: int, dimensions: List[int]):
    """ Converts vertical edge number to its co-ordinates

    Args:
        num (int): [description]
        dimensions (List[int]): [description]

    Returns:
        tuple[int, int]: [description]
    """
    if num > (dimensions[0]*(dimensions[1]+1)*2) or num < 2 or num%2 != 0:
        return None
    num = int(num/2)
    col = int(num / dimensions[0])
    row = num % dimensions[0]
    if row == 0: #last row
        row = dimensions[0]-1
        col -= 1
    else: row -= 1
    return (row, col)

def numToCoordsH(num: int, dimensions: List[int]):
    """ Converts horizontal edge number to its co-ordinates

    Args:
        num (int): [description]
        dimensions (List[int]): [description]

    Returns:
        tuple[int, int]: [description]
    """
    if num > (dimensions[1]*(dimensions[0]+1)*2-1) or num < 1 or num%2 == 0:
        return None
    num = int((num+1)/2)
    row = int(num / dimensions[1])
    col = num % dimensions[1]
    if col == 0: #last row
        col = dimensions[1]-1
        row -= 1
    else: col -= 1
    return (row, col)