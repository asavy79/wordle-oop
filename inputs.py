from abc import abstractmethod, ABC


class InputReceiver(ABC):

    def __init__(self):
        self.input_sequence = []

    @abstractmethod
    def get_input(self) -> str:
        pass


class TerminalInput(InputReceiver):

    def __init__(self):
        super().__init__()

    def get_input(self):
        return input("Enter guess: ")
