from os import remove
import numpy as np
import random
import copy

table = [[0]*9 for i in range(9)]
# table = [
# [0, 0, 5, 6, 0, 2, 0, 0, 0],
# [7, 0, 0, 8, 1, 0, 4, 0, 0],
# [0, 0, 0, 0, 0, 0, 5, 6, 0],
# [0, 4, 9, 0, 0, 0, 0, 0, 0],
# [8, 0, 0, 0, 0, 0, 0, 0, 7],
# [0, 0, 0, 0, 5, 1, 0, 0, 0],
# [0, 0, 0, 9, 4, 0, 8, 0, 2],
# [3, 0, 6, 1, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

def printTable(table):
    for rowIndex, row in enumerate(table):
        if rowIndex % 3 == 0:
            print("+-------------+-------------+-------------+")
        for columnIndex, tile in enumerate(row):
            if columnIndex % 3 == 0:
                print("|", end = ' ')
            print(f' {tile if tile != 0 else " "} ', end = ' ')
        print("|")
    print("+-------------+-------------+-------------+")

def checkPosition(table, xPos, yPos, value):
    # Check if the value exists in the row

    if (value in table[yPos]):
        return False
    
    # Check if the value exists in the column
    column = [row[xPos] for row in table]
    if (value in column):
        return False
    
    # Check if the value exists in the sub grid
    subGridX = xPos // 3
    subGridY = yPos // 3

    grid = [list(line[3*subGridX:3*subGridX+3]) for line in table[3*subGridY:3*subGridY+3]]
    for line in grid:
        if value in line:
            return False
    
    # Else return true
    return True

def findUnfilledtile(table):
    for y in range(9):
        for x in range(9):
            if (table[y][x] == 0):
                return x, y
    return -1, -1


def removeRandomTiles(table, numberToRemove):
    for i in range(numberToRemove):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        table[y][x] = 0

def fillTable(table):
    tableCopy = table.copy()
    for rowIndex, row in enumerate(tableCopy):
        for columnIndex, tile in enumerate(row):
            if (tile == 0):
                for value in range(1,10):
                    if (checkPosition(tableCopy, columnIndex, rowIndex, value)):
                        tableCopy[rowIndex][columnIndex] = value
                        if fillTable(tableCopy):
                            return True
                        tableCopy[rowIndex][columnIndex] = 0
                if tableCopy[rowIndex][columnIndex] == 0:
                    return False
            else:
                if (rowIndex == 8 and columnIndex == 8):
                    return True

def solveSudoku(table):
    x, y = findUnfilledtile(table)
    unusedNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    if y == -1: 
        return True
    
    while len(unusedNumbers) != 0:
        value = unusedNumbers[random.randint(0, len(unusedNumbers) - 1)]
        unusedNumbers.remove(value)

        if checkPosition(table, x, y, value):
            table[y][x] = value
            if solveSudoku(table):
                return True
            table[y][x] = 0
    return False

solveSudoku(table)
completeSudoku = copy.deepcopy(table)
solvable = False

while (solvable == False):
    table = copy.deepcopy(completeSudoku)
    removeRandomTiles(table, 49)
    solvable = solveSudoku(copy.deepcopy(table))

printTable(table)