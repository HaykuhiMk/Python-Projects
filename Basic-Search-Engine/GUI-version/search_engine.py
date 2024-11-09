import os
import re
from typing import List, Dict

class WordInfo:
    """
    Represents information about a word in a file.
    """
    def __init__(self, file_name : str, count: int = 0) -> None:
        self.file_name = file_name
        self.count = count

    def __lt__(self, other : "WordInfo") -> bool:
        if not isinstance(other, WordInfo):
            raise TypeError("Invalid type!")
        return self.count < other.count 
    
    def __repr__(self) -> str:
        return f"{self.file_name} - {self.count}"

class BasicSearchEngine:
    """
    A basic search engine that indexes text files and allows searching for words within them.
    """
    def __init__(self) -> None:
        """
        Initializes the search engine with empty indexes and no indexed files.
        """
        self.__index: Dict[str, List[WordInfo]] = {}
        self.__indexed_files: set = set()    

    @property
    def index(self) -> dict:
        return self.__index
    
    @index.setter
    def index(self, index : dict) -> None:
        if not isinstance(index, dict):
            raise TypeError("Invalid type!")
        self.__index = index
        
    @property
    def indexed_files(self) -> set:
        """
        Getter for the set of indexed files.
        """
        return self.__indexed_files
    
    def index_files(self, folder_path : str) -> None:
        """
        Indexes all text files in the specified folder.

        Parameters:
            folder_path (str): The path to the folder containing web page text files.
        """

        try:
            if not os.path.isdir(folder_path):
                print(f"Error: The folder '{folder_path}' does not exist.")
                return
            files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".txt")]
            for file_name in files:
                if file_name in self.__indexed_files:
                    continue
                with open(file_name, "r", encoding='utf-8') as file:
                    content = re.findall(r'\b\w+\b', file.read().lower())
                    unique_words = set(content)
                    for word in unique_words:
                        if not word in self.index:
                            self.index[word] = [WordInfo(file_name, content.count(word))]   
                        else:
                            self.index[word].append(WordInfo(file_name, content.count(word)))
                self.__indexed_files.add(file_name)

            print(f"Indexed {len(files)} web pages.")
        except FileNotFoundError:
            print(f"Error: The folder '{folder_path}' does not exist.")
        except Exception as e:
            print(f"An error occurred during indexing: {e}")

    def search(self, query : str) -> dict:
        """
        Searches for web pages containing the query words.

        Parameters:
            query (str): The search query entered by the user.

        Returns:
            List of tuples containing web page filenames and their relevance scores.
        """

        query_words = re.findall(r'\b\w+\b', query.lower())
        results: Dict[str, List[WordInfo]] = {}
        for word in query_words:
            if word in self.index:
                results[word] = self.index[word]
            else:
                print(f"'{word}' not found in the index.")
        for word, word_info in results.items():
            results[word] = sorted(word_info, key=lambda x: x.count, reverse=True)
        return results
    
    def display_search_results(self, sorted_results : dict, query : str) -> None:
        """
        Displays the search results to the user.

        Parameters:
            sorted_results (list): List of tuples containing web page filenames and scores.
            query (str): The original search` query.
        """

        for word, word_info_list in sorted_results.items():
            if word_info_list:
                print(f"\nSearch results for '{word}':")
                for wi in word_info_list:
                    print(f"{wi} match(es)") 
            else :
                print(f"'{word}' not found in the index.")
        print("-" * 40)

    def view_file_content(self) -> None:
        """
        Displays the content of the specified file if it has been indexed.
        """
        if not self.__indexed_files:
            print("No files have been indexed yet.")
            return
        
        print("\nIndexed Files:")
        indexed_file_list = sorted(os.path.basename(f) for f in self.__indexed_files)
        for idx, file_name in enumerate(indexed_file_list, start=1):
            print(f"{idx}. {file_name}")

        try:
            choice = input("\nEnter the number of the file you wish to view (or 'q' to quit): ").strip()
            if choice.lower() == 'q':
                print("Exiting file view.")
                return

            if not choice.isdigit():
                print("Invalid input. Please enter a valid number.")
                return

            choice_num = int(choice)
            if not 1 <= choice_num <= len(indexed_file_list):
                print("Number out of range. Please select a valid file number.")
                return

            selected_file = list(sorted(self.__indexed_files))[choice_num - 1]
            with open(selected_file, "r", encoding='utf-8') as file:
                content = file.read()
                print(f"\n--- Content of '{os.path.basename(selected_file)}' ---\n")
                print(content)
                print("\n--- End of File ---\n")
        except Exception as e:
            print(f"An error occurred while viewing the file: {e}")
            
    def get_indexed_files(self) -> List[str]:
        """
        Retrieves a sorted list of all indexed file paths.

        Returns:
            List[str]: List of indexed file paths.
        """
        return sorted(self.__indexed_files)

    def get_file_content(self, file_path: str) -> str:
        """
        Retrieves the content of the specified file.

        Parameters:
            file_path (str): The full path of the file to retrieve.

        Returns:
            str: The content of the file.

        Raises:
            FileNotFoundError: If the file is not indexed or does not exist.
            Exception: For any other issues during file reading.
        """
        if not file_path:
            raise ValueError("File path must be provided.")

        if file_path not in self.__indexed_files:
            raise FileNotFoundError(f"The file '{file_path}' is not indexed or does not exist.")

        try:
            with open(file_path, "r", encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the file: {e}")
