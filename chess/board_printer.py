
class BoardPrinter:

    def __init__(self, board):
        self.board = board

    def __str__(self):
        board_string = '  '

        counter = 0

        for i in range(self.board.width):
            board_string += chr(i + ord('a'))
        board_string += '\n'
        for y in range(self.board.height):
            board_string += str(self.board.height - y) + ' '
            for x in range(self.board.width):
                if self.board.squares[y][x] is not None:
                    board_string += str(self.board.squares[y][x]) if counter % 2 == 0 else str(self.board.squares[y][x])
                else:
                    board_string += ' ' if counter % 2 == 0 else '\u2588'
                counter += 1
            counter += 1
            board_string += '\n'
        return board_string
