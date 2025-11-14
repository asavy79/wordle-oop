# Wordle OOP

A command-line Wordle game built with object-oriented design principles and dependency injection.

## Features

- Classic Wordle gameplay with 6 guesses
- Color-coded feedback (correct, present, absent letters)
- Modular architecture with dependency injection
- Extensible design for different input methods and display formats

## How to Play

```bash
python main.py
```

Enter 5-letter word guesses when prompted. The game will show:
- 🟩 Green: Correct letter in correct position
- 🟨 Yellow: Correct letter in wrong position  
- ⬜ Gray: Letter not in the word

## Architecture

The game uses dependency injection to separate concerns:
- `WordleGame`: Core game logic
- `GameBoard`: Manages game state and word validation
- `InputReceiver`: Abstract interface for user input (terminal implementation included)
- `BoardDisplayer`: Abstract interface for game display (terminal implementation included)

This design makes it easy to add new input methods (GUI, web) or display formats without changing the core game logic.
