# Memory Game

## Overview
The **Memory Game** is a classic card-matching game, implemented in Python. Players flip over cards in a grid to find pairs of matching values. The game can be played in two versions: **Graphical User Interface (GUI)** using Tkinter and **Command-Line Interface (CLI)** for a simpler experience. 

The goal is to match all pairs of cards with the fewest moves and in the shortest time possible. The game keeps track of the number of moves, time elapsed, and includes a leaderboard to track high scores.

## Features
- **GUI Version**:
  - Built with Tkinter to provide an interactive and visually appealing experience.
  - Animated background that changes colors gradually.
  - Real-time timer to track how long it takes to complete the game.
  - Ability to pause and restart the game at any point.
  - Displays the number of moves taken.
  - Displays a leaderboard with high scores stored in a `leaderboard.json` file.

- **CLI Version**:
  - Text-based version that runs in the terminal.
  - Allows the user to enter grid size and card coordinates to flip cards.
  - Matches pairs of cards by typing coordinates and provides feedback.

## Files
- **`memory_game_GUI.py`**: The graphical user interface version of the Memory Game.
- **`memory_game_CLI.py`**: The command-line interface version of the Memory Game.
- **`cell.py`**: Defines a `Cell` class, which represents individual cards in the game, holding values and their matching state.

## Requirements
- Python 3.x or later
- Tkinter (for the GUI version)

To install Tkinter for your Python environment:
```bash
pip install tk
```

## How to Play

### GUI Version:
1. Run the `memory_game_GUI.py` script to launch the game.
2. A pop-up will prompt you to enter the grid size (an even number greater than 1).
3. Click on the cards to flip them over. The goal is to match all pairs.
4. The game tracks your moves and the time it takes to complete the game.
5. You can pause, restart, and view the number of moves and the timer throughout the game.

### CLI Version:
1. Run the `memory_game_CLI.py` script to start the game.
2. Enter the grid size (e.g., 4 for a 4x4 grid).
3. Use row and column numbers to flip cards and try to find matching pairs.
4. The game provides feedback on whether the flipped cards match or not.
5. The game ends when all pairs are matched.

## Leaderboard
- The GUI version saves the leaderboard in a `leaderboard.json` file. Your best performance, based on time and moves, is recorded in this file.

## License
This project is open-source and licensed under the MIT License.
