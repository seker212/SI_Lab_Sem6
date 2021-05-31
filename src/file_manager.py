from matrix import Matrix

def GetValuesFromFile(path):
    result = []
    with open(path, 'r') as file:
        content = file.readlines()
    for line in content:
        newline = line.replace("\n", "")
        result.append(newline)
    return result

def SetValuesFromFile(matrix, lines):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == ',':
                matrix.SetValue(i, j, None)
            else:
                matrix.SetValue(i, j, int(lines[i][j]))
