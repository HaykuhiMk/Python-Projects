from search_engine import BasicSearchEngine

class SearchEngineUtils:
    @staticmethod
    def display_menu():
        """Displays the main menu options to the user."""
        print("\n===== Basic Google Search Engine =====")
        print("1) Index web pages")
        print("2) Search")
        print("3) View file content")
        print("4) Exit")
        print("======================================")

    @staticmethod
    def run_search_engine():
        """Runs the search engine application, handling user input and actions."""
        search_engine = BasicSearchEngine()
        folder_path = "web_pages"  

        while True:
            SearchEngineUtils.display_menu()
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                path = input(f"Enter the folder path to index (default: '{folder_path}'): ").strip()
                if path:
                    folder_path = path
                search_engine.index_files(folder_path)

            elif choice == "2":
                if not search_engine.index:
                    print("Please index web pages first (Option 1).")
                    continue
                query = input("Enter search query: ").strip()
                if not query:
                    print("Empty query. Please enter valid search terms.")
                    continue
                results = search_engine.search(query)
                search_engine.display_search_results(results, query)

            elif choice == "3":
                if not search_engine.index:
                    print("Please index web pages first (Option 1).")
                    continue
                search_engine.view_file_content()

            elif choice == "4":
                print("Exiting search engine. Goodbye!")
                break

            else:
                print("Invalid choice, please select again.")
