import os
from datetime import date
from abc import ABC, abstractmethod
from colorama import init, Fore, Style
import re

init(autoreset=True)
# The init function initializes the colorama library, setting up any necessary configurations to allow terminal text coloring. 

class Game(ABC):
    game_id = 0

    def __init__(self, title: str, genre: str, price: float, id_developer: int):
        self.title = title
        self.genre = genre
        self.relase_date = date(2012, 1, 1)
        self.price = price
        self.id_publisher = 0
        self.id_developer = id_developer
        self.id_game = Game.game_id
        Game.game_id += 1

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str):
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not title.strip():
            raise ValueError("Title cannot be empty.")
        self._title = title.strip()

    @property
    def genre(self) -> str:
        return self._genre

    @genre.setter
    def genre(self, genre: str):
        if not isinstance(genre, str):
            raise TypeError("Genre must be a string.")
        if not genre.strip():
            raise ValueError("Genre cannot be empty.")
        self._genre = genre.strip()

    @property
    def relase_date(self) -> date:
        return self._relase_date

    @relase_date.setter
    def relase_date(self, relase_date: date):
        if not isinstance(relase_date, date):
            raise TypeError("Release date must be a date object.")
        self._relase_date = relase_date

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: float):
        if not isinstance(price, (float, int)):
            raise TypeError("Price must be a number.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self._price = float(price)

    @property
    def id_publisher(self) -> int:
        return self._id_publisher

    @id_publisher.setter
    def id_publisher(self, id_publisher: int):
        if not isinstance(id_publisher, int):
            raise TypeError("Publisher ID must be an integer.")
        if id_publisher < 0:
            raise ValueError("Publisher ID cannot be negative.")
        self._id_publisher = id_publisher

    @property
    def id_developer(self) -> int:
        return self._id_developer

    @id_developer.setter
    def id_developer(self, id_developer: int):
        if not isinstance(id_developer, int):
            raise TypeError("Developer ID must be an integer.")
        if id_developer < 0:
            raise ValueError("Developer ID cannot be negative.")
        self._id_developer = id_developer

    @property
    def id_game(self) -> int:
        return self._id_game

    @id_game.setter
    def id_game(self, id_game: int):
        if not isinstance(id_game, int):
            raise TypeError("Game ID must be an integer.")
        if id_game < 0:
            raise ValueError("Game ID cannot be negative.")
        self._id_game = id_game

    def update_release_date(self, new_release_date: date) -> None:
        self.relase_date = new_release_date
        print("Release date updated successfully.")

    @abstractmethod
    def play(self):
        ...

    def __str__(self):
        return (
            f"{Fore.CYAN}Game: {self.title}, Genre: {self.genre}, "
            f"Release Date: {self.relase_date}, Price: {self.price:.2f}, "
            f"Publisher ID: {self.id_publisher}, Developer ID: {self.id_developer}, "
            f"Game ID: {self.id_game}{Style.RESET_ALL}"
        )


class ActionGame(Game):
    def play(self):
        print(f"Launching action game: {self.title}!")
        # os.system("python3 memory_game_GUI.py")


class StrategyGame(Game):
    def play(self):
        print(f"Launching strategy game: {self.title}!")
        # os.system("python3 strategy_game_GUI.py")


class Person(ABC):
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        self._name = name.strip()

    @property
    def contact_info(self) -> str:
        return self._contact_info

    @contact_info.setter
    def contact_info(self, contact_info: str):
        if not isinstance(contact_info, str):
            raise TypeError("Contact info must be a string.")
        if not self.__is_valid_armenian_phone_number(contact_info):
            raise ValueError("Invalid Armenian phone number.")
        self._contact_info = contact_info

    def __is_valid_armenian_phone_number(self, phone_number: str) -> bool:
        pattern = r"^(\+?374|0)(10|11|33|41|43|44|46|47|49|55|77|91|93|94|95|96|98|99)\d{6}$"
        return bool(re.match(pattern, phone_number))

    @abstractmethod
    def display_info(self):
        pass


class Developer(Person):
    developer_id = 0

    def __init__(self, name: str, contact_info: str):
        super().__init__(name, contact_info)
        self.games = []
        self.id_developer = Developer.developer_id
        Developer.developer_id += 1

    def create_game(self, title: str, genre: str, price: float):
        if genre.casefold() == "strategy":
            self.games.append(StrategyGame(title, genre, price, self.id_developer))
        elif genre.casefold() == "action":
            self.games.append(ActionGame(title, genre, price, self.id_developer))
        else:
            raise ValueError("Invalid genre.")

    def update_game(self, game_title: str, new_date: date) -> None:
        for game in self.games:
            if game.title == game_title:
                game.update_release_date(new_date)
                break
        else:
            print(f"Game with title '{game_title}' not found.")

    def list_games(self):
        for game in self.games:
            print(game)

    def display_info(self):
        print(self)

    def __str__(self):
        return (f"{Fore.CYAN}Developer ID: {self.id_developer}, Name: {self.name}, "
            f"Contact: {self.contact_info}, Games: {[game.title for game in self.games]}{Style.RESET_ALL}")


class Publisher(Person):
    publisher_id = 0

    def __init__(self, name: str, contact_info: str):
        super().__init__(name, contact_info)
        self.games = []
        self.id_publisher = Publisher.publisher_id
        Publisher.publisher_id += 1

    def publish_game(self, game: Game):
        if not isinstance(game, Game):
            raise TypeError("Only instances of Game can be published.")
        game.id_publisher = self.id_publisher
        self.games.append(game)
        print(f"Game '{game.title}' published by {self.name}!")

    def display_info(self):
        print(self)

    def __str__(self):
        return (f"{Fore.CYAN}Publisher ID: {self.id_publisher}, Name: {self.name}, "
            f"Contact: {self.contact_info}, Published Games: {[game.title for game in self.games]}{Style.RESET_ALL}")


class Platform:
    def __init__(self, name: str):
        self.name = name
        self.games = []
        self.developers = []
        self.publishers = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Platform name must be a string.")
        if not name.strip():
            raise ValueError("Platform name cannot be empty.")
        self._name = name.strip()

    def add_developer(self, developer: Developer):
        if not isinstance(developer, Developer):
            raise TypeError("Only instances of Developer can be added.")
        self.developers.append(developer)
        print(f"Developer '{developer.name}' added to platform '{self.name}'.")

    def add_publisher(self, publisher: Publisher):
        if not isinstance(publisher, Publisher):
            raise TypeError("Only instances of Publisher can be added.")
        self.publishers.append(publisher)
        print(f"Publisher '{publisher.name}' added to platform '{self.name}'.")

    def add_game(self, game: Game):
        if not isinstance(game, Game):
            raise TypeError("Only instances of Game can be added.")
        self.games.append(game)
        print(f"Game '{game.title}' added to platform '{self.name}'.")

    def list_games(self):
        print(f"Games on platform '{self.name}':")
        for game in self.games:
            print(game)

    def list_developers(self):
        print(f"Developers on platform '{self.name}':")
        for developer in self.developers:
            developer.display_info()

    def list_publishers(self):
        print(f"Publishers on platform '{self.name}':")
        for publisher in self.publishers:
            publisher.display_info()

