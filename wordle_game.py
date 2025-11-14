import random
from inputs import InputReceiver
from game_board import GameBoard


class WordleGame:
    def __init__(self, guesses: int, word_bank: list[str], board: GameBoard, input_receiver: InputReceiver):
        self.guesses = guesses
        self.word_bank = word_bank
        self.board = board

        self.target_word = None
        self.current_guess = 0
        self.input_receiver = input_receiver

    def _get_random_word(self):
        return random.choice(self.word_bank)

    def play(self):
        self._reset()
        self.target_word = self._get_random_word()

        while self.current_guess < self.guesses:
            guess = self.get_input()
            self.play_turn(guess)
            self.display_board()
            if self.check_win(guess):
                print(f"WINNER in {self.current_guess} attempts")
                return

        print("LOSER")
        print(f"Word was: {self.target_word}")

    def check_win(self, guess):
        return guess == self.target_word

    def play_turn(self, guess: str):
        if len(guess) != len(self.target_word):
            raise Exception("Invalid word length!")
        self.board.add_word(guess, self.target_word)
        self.current_guess += 1

    def display_board(self):
        self.board.display()

    def _reset(self):
        self.current_guess = 0
        self.board.reset()
        pass

    def get_input(self) -> str:
        return self.input_receiver.get_input().upper()
