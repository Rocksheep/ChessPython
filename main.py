from chess.board import Board
from chess.board_printer import BoardPrinter

if __name__ == '__main__':
    board_printer = BoardPrinter(Board())
    print(board_printer)
