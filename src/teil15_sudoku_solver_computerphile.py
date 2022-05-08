# import random
"""
Stolen from 'Conceptual Programming'
A much more elegant Solution!
"""

class ClassName:
    def __init__(self):
        self.grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]

    def create_empty_sudoku(self):
        e = [[0] * self.no_of_rows for _ in range(self.no_of_columns)]
        return e

    def read_sudoku(self, path : str):
        pass

    def possible(self, y : int, x : int, n : int):

        for i in range(0, 9):
            if self.grid[y][i] == n:
                return False
        for i in range(0, 9):
            if self.grid[i][x] == n:
                return False
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if self.grid[y0 + i][x0 + j] == n:
                    return False
        return True

    def solve(self):

        for y in range(0, 9):
            for x in range(0, 9):
                if self.grid[y][x] == 0:
                    for n in range(1, 10):
                        if self.possible(y, x, n):
                            self.grid[y][x] = n
                            self.solve()
                            self.grid[y][x] = 0
                    return
        self.print_grid()

    def print_grid(self):
        for line in self.grid:
            for square in line:
                if square == 0:
                    print(".", end=" ")
                else:
                    print(square, end=" ")
            print()


def main():
    cn = ClassName()
    cn.solve()


if __name__ == "__main__":
    main()
