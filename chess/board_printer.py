
class BoardPrinter:

    def __init__(self, board):
        self.board = board

    def __str__(self):
        board_string = ''

        counter = 0

        for y in range(self.board.height):
            for x in range(self.board.width):
                if y == 1:
                    board_string += ' \u265F '
                elif y == 6:
                    board_string += ' \u2659 '
                else:
                    board_string += '   ' if counter % 2 == 0 else '\u2588\u2588\u2588'
                counter += 1
            counter += 1
            board_string += '\n'
        return board_string
