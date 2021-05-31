from typing import List

def coordsToNumV(row: int, col: int, dimensions: List[int]):
    """Converts vertical edge co-ordinates to its number

    Args:
        row (int): [description]
        col (int): [description]
        dimensions (List[int]): [description]

    Returns:
        Optional[int]: [description]
    """

    if row >= dimensions[0] or col > dimensions[1]:
        return None
    return col * dimensions[0] + row+1

def coordsToNumH(row: int, col: int, dimensions: List[int]):
    """ Converts horizontal edge co-ordinates to its number

    Args:
        row (int): [description]
        col (int): [description]
        dimensions (List[int]): [description]

    Returns:
        Optional[int]: [description]
    """
    if row > dimensions[0] or col >= dimensions[1]:
        return None
    return row * dimensions[1] + col+1

def numToCoordsV(num: int, dimensions: List[int]):
    """ Converts vertical edge number to its co-ordinates

    Args:
        num (int): [description]
        dimensions (List[int]): [description]

    Returns:
        tuple[int, int]: [description]
    """
    if num > dimensions[0]*(dimensions[1]+1):
        return None
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
    if num > dimensions[1]*(dimensions[0]+1):
        return None
    row = int(num / dimensions[1])
    col = num % dimensions[1]
    if col == 0: #last row
        col = dimensions[1]-1
        row -= 1
    else: col -= 1
    return (row, col)

#TODO:
#change dimensions value to its final versions
