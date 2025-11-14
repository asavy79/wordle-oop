from wordle_game import WordleGame
from inputs import TerminalInput
from game_board import GameBoard
from board_displayer import TerminalDisplayer

WORDS = [
    "APPLE", "BRAVE", "CHAIR", "DANCE", "EAGER", "FAITH", "GRAIN", "HONEY", "IVORY", "JOKER",
    "KNIFE", "LEMON", "MAGIC", "NOBLE", "OASIS", "PAPER", "QUICK", "RIVER", "SHINE", "TIGER",
    "UNION", "VIVID", "WATER", "XENON", "YOUTH", "ZEBRA", "ACORN", "BLADE", "CLOUD", "DRIVE",
    "ELITE", "FROST", "GLASS", "HEART", "INPUT", "JUDGE", "KNEEL", "LIGHT", "MIGHT", "NIGHT",
    "OPERA", "PRIDE", "QUEST", "ROBIN", "SMILE", "TRUST", "URBAN", "VOICE", "WHEEL", "XENIA",
    "YACHT", "ZONED", "ANGEL", "BLEND", "CRISP", "DELTA", "EVENT", "FRAME", "GIANT", "HABIT",
    "INDEX", "JELLY", "KOALA", "LEVEL", "MODEL", "NURSE", "OCEAN", "PLANT", "QUILT", "RANCH",
    "SWEET", "THING", "UNDER", "VIRAL", "WORLD", "XERIC", "YIELD", "ZAPPY", "ALERT", "BERRY",
    "CROWN", "DEMON", "EMBER", "FUNNY", "GRACE", "HUMAN", "IDEAL", "JUMBO", "KARMA", "LUNCH",
    "METAL", "NOVEL", "ORBIT", "PEARL"
]


if __name__ == "__main__":

    displayer = TerminalDisplayer()
    terminal_receiver = TerminalInput()
    board = GameBoard(displayer=displayer)
    game = WordleGame(guesses=6, word_bank=WORDS, board=board,
                      input_receiver=terminal_receiver)

    game.play()
