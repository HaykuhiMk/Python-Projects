import os
import re

class WordInfo:
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
    def __init__(self) -> None:
        """
        Initializes the search engine with empty indexes.
        """
        self.__index = {}       

    @property
    def index(self) -> dict:
        return self.__index
    
    @index.setter
    def index(self, index : dict) -> None:
        if not isinstance(index, dict):
            raise TypeError("Invalid type!")
        self.__index = index
        
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
                with open(file_name, "r", encoding='utf-8') as file:
                    content = re.findall(r'\b\w+\b', file.read().lower())
                    unique_words = set(content)
                    for word in unique_words:
                        if not word in self.index:
                            self.index[word] = [WordInfo(file_name, content.count(word))]   
                        else:
                            self.index[word].append(WordInfo(file_name, content.count(word)))

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
        results = {}
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
        while True:
            file_name = input("Enter the name of the file you wish to view: ").strip()
            
            if not file_name:
                print("Please enter a valid file name.")
                continue
            
            if not os.path.isfile(file_name):
                print(f"Error: The file '{file_name}' does not exist or was not indexed.")
                retry = input("Do you want to try again? (y/n): ").strip().lower()
                if retry == 'y':
                    continue
                else:
                    break
            try:
                with open(file_name, "r", encoding='utf-8') as file:
                    print(f"\nContent of '{file_name}':")
                    print(file.read())
            except Exception as e:
                print(f"An error occurred while reading the file: {e}")
            break
