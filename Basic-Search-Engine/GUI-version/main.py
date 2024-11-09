import tkinter as tk
from search_engine_GUI import SearchEngineGUI

def main():
    root = tk.Tk()
    app = SearchEngineGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

