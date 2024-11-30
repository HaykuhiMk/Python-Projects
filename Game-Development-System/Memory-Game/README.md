# Memory Game

## Overview
The **Memory Game** is a Python-based card-matching game where players flip cards to find matching pairs. It offers two modes of play: a **Graphical User Interface (GUI)** for an interactive experience and a **Command-Line Interface (CLI)** for a straightforward text-based approach. The game tracks your time, moves, and leaderboard scores.

## Features
- Adjustable grid size (even numbers only).
- Two gameplay modes: GUI and CLI.
- Real-time timer and move counter in the GUI version.
- Leaderboard for tracking high scores.
- Animated background in the GUI.

## Files
- **`memory_game_GUI.py`**: The GUI version.
- **`memory_game_CLI.py`**: The CLI version.
- **`cell.py`**: Defines the `Cell` class for game logic.

## Requirements
Python 3.x or later
Tkinter (for the GUI version)
To install Tkinter for your Python environment:

```pip install tk```

## Dependencies
This project requires the following Python libraries:
- `tkinter` (for GUI components)
- `numpy` (for grid and cell management)
- `json` (for leaderboard storage)
- `os` (for system operations)
- `time` (for delay in the CLI version)

To install required dependencies, ensure you have Python 3.x installed and run:
```bash
pip install numpy
```
(Note: `tkinter` is included by default in most Python installations.)

## How to Play

### GUI Version:
1. Run `memory_game_GUI.py` to start the game.
2. Enter the grid size when prompted (even numbers greater than 1).
3. Click cards to flip them over, matching pairs.
4. Pause, restart, and view the timer and move count as needed.

### CLI Version:
1. Run `memory_game_CLI.py`.
2. Enter the grid size.
3. Use row and column coordinates to select and flip cards.

## Leaderboard
The GUI stores scores in `leaderboard.json`. You can view and track top times and move counts.

## License
This project is open-source and licensed under the MIT License.
