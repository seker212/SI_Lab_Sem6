import os, sys
sys.path.append(os.getcwd())

from src.file_manager import *

if __name__ == '__main__':
    filename = 'matrix.txt'
    pre_val_matrix = GetValuesFromFile(filename)
    val_matrix = Matrix(pre_val_matrix[0].count(',')+1, len(pre_val_matrix))
    SetValuesFromFile(val_matrix, pre_val_matrix)
    