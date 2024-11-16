# Game Management System

This repository contains a Python implementation of a **Game Management System** that simulates interactions between developers, publishers, and a platform to manage games. The system includes functionality for creating, publishing, and listing games, and enforces good coding practices such as encapsulation, modularity, and validation.

---

## Features

### 1. **Game Management**
- **Base Class**: `Game` (Abstract Base Class)
  - Attributes: `title`, `genre`, `release_date`, `price`, `id_developer`, `id_publisher`, `id_game`.
  - Methods: Getters, setters, `update_release_date()`, and an abstract method `play()`.
- **Subclasses**:
  - `ActionGame`: Implements the `play()` method for action games.
  - `StrategyGame`: Implements the `play()` method for strategy games.

### 2. **Person Management**
- **Base Class**: `Person` (Abstract Base Class)
  - Attributes: `name`, `contact_info`.
  - Validation: Ensures valid names and Armenian phone numbers.
  - Abstract Method: `display_info()`.

- **Developer**: 
  - Attributes: `games`, `id_developer`.
  - Methods: `create_game()`, `update_game()`, `list_games()`.
  - Developers can create and manage their own games.

- **Publisher**: 
  - Attributes: `games`, `id_publisher`.
  - Methods: `publish_game()`, `list_games()`.
  - Publishers can publish games created by developers.

### 3. **Platform Management**
- Centralized class for managing:
  - Games (`add_game()`, `list_games()`).
  - Developers (`add_developer()`, `list_developers()`).
  - Publishers (`add_publisher()`, `list_publishers()`).

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Game-Management-System.git
   cd Game-Management-System
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Dependencies include:
   - `colorama`: For colored terminal output.

3. Run the system:
   ```bash
   python main.py
   ```

---

## Usage

1. **Create a Platform**:
   ```python
   platform = Platform("Gaming Hub")
   ```

2. **Add Developers**:
   ```python
   dev1 = Developer("John Doe", "+37493987654")
   platform.add_developer(dev1)
   ```

3. **Develop Games**:
   ```python
   dev1.create_game("Action Hero", "Action", 59.99)
   dev1.create_game("Chess Master", "Strategy", 29.99)
   ```

4. **Publish Games**:
   ```python
   publisher = Publisher("XYZ Publishing", "+37491987654")
   platform.add_publisher(publisher)

   # Publish a game
   game = dev1.games[0]
   publisher.publish_game(game)
   ```

5. **List Games, Developers, or Publishers**:
   ```python
   platform.list_games()
   platform.list_developers()
   platform.list_publishers()
   ```

---

## Code Highlights

### Encapsulation
- Private attributes with getters and setters for validation.
- Abstract methods ensure implementation of core functionality in subclasses.

### Validation
- Titles and genres are checked for valid strings.
- Armenian phone numbers are validated using regex.

### Modularity
- Independent classes: `Game`, `Person`, `Developer`, `Publisher`, and `Platform`.

---

## Future Extensions

1. Add new game genres (e.g., `AdventureGame`, `SportsGame`) by subclassing `Game`.
2. Extend platform functionality to:
   - Support user reviews.
   - Include game sales and analytics.
3. Add support for multiplayer games with a `MultiplayerGame` class.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
