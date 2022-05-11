# import random
import sys

class ClassName:
    """
    Sudoku is Grütze ...
    Sudoku sucks (as they say in the free world)
    """

    def __init__(self):
        self.no_of_rows = 9
        self.no_of_columns = 9

        self.board = dict()
        self.rows = list()
        self.columns = list()
        self.blocks = list()
        self.free_squares = set()
        self.a_sudoku = None

    def index_to_position(self, i):
        row = i // 9
        column = i % 9
        block = row // 3 * 3 + column // 3
        return (column, row, block)

    # TODO occupie should add
    def occupie_field(self, position, value):
        column, row, block = position
        self.columns[column].remove(value)
        self.rows[row].remove(value)
        self.blocks[block].remove(value)
        self.free_squares.remove(position)
        self.board[position] = value
    
    # TODO clear should remove
    def clear_field(self, position, value):
        column, row, block = position
        self.columns[column].add(value)
        self.rows[row].add(value)
        self.blocks[block].add(value)
        self.free_squares.add(position)
        self.board[position] = 0

    def find_candidate_field(self):
        least_count_of_candidates = 9 # max count -> row/column is empty
        for position in self.free_squares:
            column, row, block = position
            candidates = self.columns[column] & self.rows[row] & self.blocks[block]
            candidate_count = len(candidates)
            if candidate_count < 2:
                return position, candidates

            if candidate_count < least_count_of_candidates:
                candidate_field = (position, candidates)
                least_count_of_candidates = candidate_count
        
        return candidate_field

    def setup(self):
        for i in range(9):
            self.columns.append({1, 2, 3, 4, 5, 6, 7, 8, 9})
            self.rows.append({1, 2, 3, 4, 5, 6, 7, 8, 9})
            self.blocks.append({1, 2, 3, 4, 5, 6, 7, 8, 9})

        for i in range(81):
            self.free_squares.add(self.index_to_position(i))

    def read_sudoku(self, sudoku):
        for i, letter in enumerate(sudoku):
            if letter in ['.', '0']:
                self.board[self.index_to_position(i)] = 0
            else:
                self.occupie_field(self.index_to_position(i), int(letter))

    def solve(self):
        if not self.free_squares:
            return True
        position, candidates = self.find_candidate_field()
        for candidate in candidates:
            self.occupie_field(position, candidate)
            if self.solve():
                return True
            self.clear_field(position, candidate)

    def print_board(self):
        for i in range(81):
            pos = self.index_to_position(i)
            print(self.board[pos], end=' ')
            if (i+1) % 9 == 0:
                print()

def main():
    if len(sys.argv) < 2:
        print("Ui...")
        sys.exit(-1)
    else:
        cn = ClassName()
        cn.setup()

        with open("./data/Teil_15_Sudoku_top20_hard.txt", 'r') as f:
            sudokus = f.readlines()

        index = int(sys.argv[1])
        cn.read_sudoku(sudokus[index].strip())
        # position, candidates = cn.find_candidate_field()
        cn.solve()
        cn.print_board()
    
    # FIXME : loop gives KeyError ...
    # for i in range(3):
    #     cn.setup()
    #     cn.read_sudoku(sudokus[i].strip())
    #     cn.solve()
    #     cn.print_board()


if __name__ == "__main__":
    main()
