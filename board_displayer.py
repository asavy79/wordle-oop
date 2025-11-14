from abc import ABC, abstractmethod
from utils import YELLOW, GREEN, RESET, CellStatus


class BoardDisplayer(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def display(self, board):
        pass


class TerminalDisplayer(BoardDisplayer):

    def __init__(self):
        super().__init__()

    def display(self, board):
        for row in board:
            self._print_row(row)

    def _print_row(self, row: list[tuple]):
        row_output = []
        for status, chr in row:
            if status == CellStatus.CORRECT:
                color_code = GREEN
            elif status == CellStatus.PRESENT:
                color_code = YELLOW
            else:
                color_code = ""

            row_output.append(color_code + chr + RESET)
        print("-".join(row_output))
