dimensions = [3,4] #rows, cols - example variables

# Converts vertical edge co-ordinates to its number
def coordsToNumV(row, col):
    if row >= dimensions[0] or col > dimensions[1]:
        return None
    return col * dimensions[0] + row+1

# Converts horizontal edge co-ordinates to its number
def coordsToNumH(row, col):
    if row > dimensions[0] or col >= dimensions[1]:
        return None
    return row * dimensions[1] + col+1

# Converts vertical edge number to its co-ordinates
def numToCoordsV(num):
    if num > dimensions[0]*(dimensions[1]+1):
        return None
    col = int(num / dimensions[0])
    row = num % dimensions[0]
    if row == 0: #last row
        row = dimensions[0]-1
        col -= 1
    else: row -= 1
    return (row, col)

# Converts horizontal edge number to its co-ordinates
def numToCoordsH(num):
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

#tests
"""
print("-----")
print(coordsToNumV(0,0))
print(coordsToNumV(1,0))
print(coordsToNumV(0,2))
print(coordsToNumV(1,2))
print(coordsToNumV(2,3))
print(coordsToNumV(3,3))
print(coordsToNumV(2,4))

print("-----")
print(coordsToNumH(0,0))
print(coordsToNumH(0,2))
print(coordsToNumH(3,0))
print(coordsToNumH(3,2))
print(coordsToNumH(4,1))
print(coordsToNumH(2,3))

print("-----")
print(numToCoordsV(1))
print(numToCoordsV(2))
print(numToCoordsV(7))
print(numToCoordsV(8))
print(numToCoordsV(9))
print(numToCoordsV(11))
print(numToCoordsV(12))
print(numToCoordsV(13))
print(numToCoordsV(15))

print("-----")
print(numToCoordsH(1))
print(numToCoordsH(3))
print(numToCoordsH(10))
print(numToCoordsH(12))
print(numToCoordsH(13))
print(numToCoordsH(15))
"""