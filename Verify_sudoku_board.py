from typing import List

# Given a 9x9 matrix signifying a partially completed sudoku board, verify if it adhears to the rules of sudoku
# each row, column and 3x3 block should not have only 1-9 numbers with no repetitions (empty spaces are represented as 0)
def check_validity(grid: List[List[int]]) -> bool:

    col_hashsets = [set() for _ in range(9)]
    subgrid_hashsets = [[set() for _ in range(3)] for _ in range(3)]
    for i, row in enumerate(grid):
        hashset = set()
        for j, item in enumerate(row):
            if item == 0:
                continue

            if item in hashset:             # check if there is repetition in rows (same logic as Pair_sum-unsorted, using hashsets)
                return False   
            hashset.add(item)

            if item in col_hashsets[j]:     # check if there is repetition in columns 
                return False
            col_hashsets[j].add(item)

            if item in subgrid_hashsets[i//3][j//3]:            # check if there is repetition in sub grids
                return False
            subgrid_hashsets[i//3][j//3].add(item)

    return True

grid = [[3, 0, 6, 0, 5, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [1, 0, 2, 5, 0, 0, 3, 2, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [0, 3, 0, 0, 0, 8, 2, 5, 0],
        [0, 1, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 0, 0, 0],
        ]

print(check_validity(grid))