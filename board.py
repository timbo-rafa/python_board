from itertools import repeat

class Cell:
    def __init__(self, i, j, value):
        self.i = i
        self.j = j
        self.value = value
    def __eq__(self, other):
        return self.i == other.i and self.j == other.j
    def __hash__(self):
        return hash((self.i, self.j))

class Path:
    def __init__(self, current, board, used = None, number = None):
        self.board = board
        self.used = used if used else set()
        self.used.add(current)
        self.current = current
        self.number = number if number else current.value

    def find_next(self):
        i = self.current.i
        j = self.current.j

        neighbors = []
        # above
        if i > 0:
            above = Cell(i - 1, j, self.board[ i - 1][j])
            neighbors.append(above)
        
        # right
        if j < len(self.board[0]) - 1:
            right = Cell(i, j + 1, self.board[i][j + 1])
            neighbors.append(right)
        
        # below
        if i < len(self.board) - 1:
            below = Cell(i + 1, j, self.board[i + 1] [j])
            neighbors.append(below)

        # left
        if j > 0:
            left = Cell(i, j - 1, self.board[ i][j - 1])
            neighbors.append(left)

        neighbors = [cell for cell in neighbors if cell not in self.used]

        # stop on a dead end
        if len(neighbors) == 0:
            self.next_number = self.number
            self.next = [self.current]
            return

        max_neighbor = max(neighbors, key=lambda cell: cell.value)

        next_cells = [cell for cell in neighbors if cell.value == max_neighbor.value]
        
        self.next_number = int(str(self.number) + str(max_neighbor.value))
        self.next = [
            Path(nc, self.board, self.used.copy(), self.next_number)
            for nc in next_cells
        ]

def solution(Board, numberOfDigits=4):

    cells_by_number = [ set() for _ in range(10)]
    for i, line in enumerate(Board):
        for j, n in enumerate(line):
            cell = Cell(i, j, n)
            cells_by_number[n].add(cell)

    cur_paths = []
    for start in range(9, 0, -1):
        current_set = cells_by_number[start]
        if (len(current_set) > 0):
            for cell in current_set:
                path = Path(cell, Board)
                cur_paths.append(path)
            break

    del cells_by_number

    number_digits = 4
    for _ in repeat(None, number_digits - 1):
        maximal_number = 0
        for cur in cur_paths:
            cur.find_next()
            maximal_number = max(maximal_number, cur.next_number)
        
        # filter paths with maximal number
        cur_paths = [path for path in cur_paths if path.next_number == maximal_number]
        # update current paths
        cur_paths = [path for cur in cur_paths for path in cur.next]
    
    ans = 0
    if len(cur_paths) > 0:
        ans = int(cur_paths[0].number)
    
    return ans

# d = number of digits of answer
# n = size of board
#
# O (n * 4^(d-1))
#
# Algorithm
# go through all cells, start looking for path on greatest-digit cells.
# Each cell may generate up to 4 solutions if neighbor digits are all the same.
# This means the possible solutions may quadruplicate per added digit.
# However, this is the worse case, and when a greater number is found,
# lesser solutions are filtered out.
# 