# Basic Search Engine

This project implements a simple text-based search engine using Python. It indexes text files and allows users to search for words within those files, displaying the relevance based on the frequency of occurrence. The search engine mimics a basic search functionality by indexing files in a specified folder and then allowing users to search for words in those files.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Class Descriptions](#class-descriptions)
- [How to Run](#how-to-run)
- [Example Usage](#example-usage)
- [Future Improvements](#future-improvements)

## Features
- **File Indexing:** Indexes text files from a specified folder, storing the frequency of each word in each file.

- **Search Functionality:** Allows users to search for words and displays the relevant files sorted by word frequency.

- **View Indexed File Content:** Users can view the content of indexed files directly.

- **nteractive Menu:** Provides a simple menu interface for users to navigate through different options.

## Technologies Used
- **Python:** The project is written entirely in Python, utilizing core libraries such as os and re for file management and regular expressions.

## Project Structure
- **search_engine.py:** Contains the core functionality for the search engine, including indexing files, searching for words, and displaying results.

- **search_engine_utils.py:** Provides the user interface and manages the interaction with the BasicSearchEngine class.

- **WordInfo:** A helper class that stores information about a word’s occurrence in a file, including the file name and count.

## Class Descriptions
- **BasicSearchEngine:** Manages file indexing and search functionality.
Uses a dictionary to store indexed words and their associated WordInfo objects.

- **WordInfo:** Represents the frequency of a word in a specific file.
Contains attributes for the file name and word count.
## How to Run
### 1. Clone the Repository:
```git clone https://github.com/HaykuhiMk/Basic-Search-Engine.git```

```cd ./Basic-Search-Engine/CLI-version/```

### 2. Run the Search Engine:
```python3 main.py```

## Example Usage
- **Index Files:**
The search engine will automatically index all .txt files in the specified folder.
It will store the occurrence of each unique word in those files.

- **Search for a Word:**
Enter the search query, and the engine will display files where the word is found, sorted by word frequency.

- **View File Content:**
You can view the full content of any indexed file by entering its name.

## Future Improvements
- Add support for more file types (e.g., HTML, PDF).

- Implement a more sophisticated relevance algorithm.

- Enhance the user interface with more detailed search analytics.

## Contributing
Contributions are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.
