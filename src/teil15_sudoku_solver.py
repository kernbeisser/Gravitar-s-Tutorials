# import random


class ClassName:
    """
    Sorry pal, but this is pfff ...
    i happen to hae a solution from 2006, back when i was beeing 
    educated as a developer.
    """
    def __init__(self):
        self.no_of_rows = 9
        self.no_of_columns = 9

        self.board = dict()
        self.rows = list()
        self.columns = list()
        self.blocks = list()
        self.free_squares = set()

    def setup(self):
        print("much ado about not much ...")

    def index_to_position(self, i):
        row = i // 9
        column = i % 9
        block = row // 3 * 3 + column // 3
        return column, row, block


def main():
    cn = ClassName()
    cn.setup()


if __name__ == "__main__":
    main()
