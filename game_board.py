from board_displayer import BoardDisplayer
from utils import CellStatus


class GameBoard:

    def __init__(self, displayer: BoardDisplayer):
        self.board = []
        self.displayer = displayer

    def add_word(self, guess: str, actual_word: str):
        self.board.append(self._create_row(guess, actual_word))

    def _create_row(self, guess: str, actual_word: str):
        new_row = [None for _ in range(len(guess))]
        for i in range(len(guess)):
            if guess[i] == actual_word[i]:
                status = CellStatus.CORRECT
            elif guess[i] in actual_word:
                status = CellStatus.PRESENT
            else:
                status = CellStatus.ABSENT
            new_row[i] = (status, guess[i].upper())
        return new_row

    def display(self):
        self.displayer.display(self.board)

    def reset(self):
        self.board = []
