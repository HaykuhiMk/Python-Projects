from game_managment_system import *

dev1 = Developer("John Doe", "+37499123456")
dev2 = Developer("Jane Smith", "+37498123456")

pub1 = Publisher("Gaming World", "+37499123457")
pub2 = Publisher("Epic Games", "+37498123457")

platform = Platform("SuperPlatform")

platform.add_developer(dev1)
platform.add_developer(dev2)
platform.add_publisher(pub1)
platform.add_publisher(pub2)

dev1.create_game("Action Hero", "action", 49.99)
dev1.create_game("Battlefield", "strategy", 39.99)

dev2.create_game("Space Adventure", "action", 59.99)
dev2.create_game("Chess Masters", "strategy", 29.99)

platform.add_game(dev1.games[0])
platform.add_game(dev1.games[1])
platform.add_game(dev2.games[0])
platform.add_game(dev2.games[1])

platform.list_developers()
platform.list_publishers()
platform.list_games()

dev1.update_game("Action Hero", date(2024, 5, 15))

pub1.publish_game(dev1.games[0])
pub1.publish_game(dev2.games[1])

pub1.display_info()

try:
    dev1.create_game("Invalid Game", "puzzle", 20.00)  # Invalid genre
except ValueError as e:
    print(f"Error: {e}")

try:
    pub1.publish_game("NonGame")  # Invalid game instance
except TypeError as e:
    print(f"Error: {e}")

try:
    dev1.contact_info = "+37412345"  # Invalid Armenian phone number
except ValueError as e:
    print(f"Error: {e}")

try:
    dev1.create_game("", "action", 45.00)  # Invalid title
except ValueError as e:
    print(f"Error: {e}")

try:
    dev1.create_game("New Game", "", 45.00)  # Invalid genre
except ValueError as e:
    print(f"Error: {e}")

