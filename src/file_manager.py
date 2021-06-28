from src.matrix import Matrix
import re

def GetValuesFromFile(path):
    result = []
    with open(path, 'r') as file:
        content = file.readlines()
    for line in content:
        x = re.match('^[0-3\,]*$',line)
        if x is None:
            return None
        newline = line.replace("\n", "")
        result.append(newline)
    return result

def SetValuesFromFile(matrix, lines):
    for i in range(len(lines)):
        splitted = lines[i].split(',')
        for j in range(len(splitted)):
            # if lines[i][j] == ',':
            #     matrix.SetValue(i, j, None)
            if splitted[j] == '':
                matrix.SetValue(i, j, None)
            else:
                matrix.SetValue(i, j, int(splitted[j]))
