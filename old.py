def pickDirection(Board = [[]], cell):
    n, i, j = cell

    maxJ = len(Board[0]) - 1
    maxI = len(Board) - 1
    above = (i - 1, j)
    right = (i, j + 1)
    below = (i + 1, j)
    left  = (i , j - 1)

    aboveNumber = -1
    rightNumber = -1
    belowNumber = -1
    leftNumber = -1

    if  i > 0:
        aboveNumber = Board[ i - 1][j]
        
    if j < maxJ:
        rightNumber = Board[i][j + 1]
    
    if i < maxI:
        belowNumber = Board[i + 1] [j]

    if j > 0:
        leftNumber  = Board[ i][j - 1]

    m = max(aboveNumber, rightNumber, belowNumber, leftNumber)


def solution(Board):
    Board = [[1]]

    cellsByNumber = [ set() for _ in range(10)]
    for i in Board:
        for j in i:
            cellsByNumber[j].add((j, i, j))

    candidates = []
    for start in range(9, 0, -1):
        currentSet = cellsByNumber[start]
        if (len(currentSet) > 0):
            for cell in currentSet:
                candidates.append(cell)

