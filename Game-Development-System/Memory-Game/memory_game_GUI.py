import tkinter as tk
from tkinter import messagebox, simpledialog
import numpy as np
from cell import Cell
import json
import os

class MemoryGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")
        self.root.configure(bg="lightblue")
        self.root.resizable(True, True)
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", self.toggle_fullscreen)

        self.__size = 4
        self.__win_case = (self.__size ** 2) // 2
        self.__first_click = None
        self.__second_click = None
        self.__board = None
        self.colors = ["#ADD8E6", "#87CEEB", "#00BFFF", "#1E90FF", "#4682B4"]
        self.color_index = 0
        self.steps = 100
        self.current_step = 0

        self.move_count = 0
        self.timer_seconds = 0
        self.timer_running = True

        self.leaderboard_file = "leaderboard.json"
        self.__load_leaderboard()

        self.animate_background()
        self.__input_size()
        self.__init_board()
        self.__create_widgets()
        self.__start_timer()

    def hex_to_rgb(self, hex_color):
        """Convert hex color to RGB tuple."""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(self, rgb_color):
        """Convert RGB tuple to hex color."""
        return f"#{rgb_color[0]:02x}{rgb_color[1]:02x}{rgb_color[2]:02x}"

    def interpolate_color(self, color1, color2, factor):
        """Calculate the intermediate color by interpolating between two colors."""
        return tuple(int(color1[i] + (color2[i] - color1[i]) * factor) for i in range(3))

    def animate_background(self):
        """Animate background color smoothly by interpolating between colors."""
        color1 = self.hex_to_rgb(self.colors[self.color_index])
        color2 = self.hex_to_rgb(self.colors[(self.color_index + 1) % len(self.colors)])
        factor = self.current_step / self.steps
        new_color = self.interpolate_color(color1, color2, factor)
        hex_color = self.rgb_to_hex(new_color)
        self.root.configure(bg=hex_color)
        self.current_step += 1
        if self.current_step > self.steps:
            self.current_step = 0
            self.color_index = (self.color_index + 1) % len(self.colors)
        self.root.after(30, self.animate_background)

    def toggle_fullscreen(self, event=None):
        """Toggle fullscreen mode."""
        current_state = self.root.attributes('-fullscreen')
        self.root.attributes('-fullscreen', not current_state)

    def __input_size(self):
        """Prompt the user for a board size."""
        input_window = tk.Toplevel(self.root)
        input_window.title("Input Grid Size")
        input_window.transient(self.root)
        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()
        input_width = 450
        input_height = 250
        position_top = (root_height // 2) - (input_height // 2)
        position_left = (root_width // 2) - (input_width // 2)

        input_window.geometry(f"{input_width}x{input_height}+{position_left}+{position_top}")
        label = tk.Label(input_window, text="Enter the grid size (even number):",
                        font=("Helvetica", 22, "bold"))
        label.pack(pady=40)

        entry = tk.Entry(input_window, width=16, font=("Helvetica", 22))
        entry.pack(pady=5)

        def on_ok_click():
            size = entry.get()
            try:
                size = int(size)
                if size % 2 == 0 and size >= 2:
                    self.__size = size
                    self.__win_case = (self.__size ** 2) // 2
                    input_window.destroy()
                else:
                    messagebox.showerror("Invalid Input",
                                        "Size must be an even number greater than 1.")
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid number.")
        ok_button = tk.Button(input_window, text="OK",
                            command=on_ok_click, height=1, font=("Helvetica", 16))
        ok_button.pack(pady=10)
        input_window.grab_set()
        self.root.wait_window(input_window)

    def __init_board(self):
        """Initialize and shuffle the game board with pairs of matching cells."""
        cells = np.array([*[Cell(i) for i in range(1, self.__win_case + 1)],
                          *[Cell(i) for i in range(1, self.__win_case + 1)]])
        np.random.shuffle(cells)
        self.__board = cells.reshape(self.__size, self.__size)

    def __create_widgets(self):
        """Create the board buttons and initialize the game layout."""
        self.buttons = []
        self.board_frame = tk.Frame(self.root, bg="lightblue")
        self.board_frame.pack(expand=True, fill=tk.BOTH)

        self.info_frame = tk.Frame(self.root, bg="lightblue")
        self.info_frame.pack(side=tk.TOP, fill=tk.X)

        self.timer_label = tk.Label(self.info_frame, text="Time: 0",
                                    font=("Helvetica", 16), bg="lightblue")
        self.timer_label.pack(side=tk.LEFT, padx=10)

        self.moves_label = tk.Label(self.info_frame, text="Moves: 0",
                                    font=("Helvetica", 16), bg="lightblue")
        self.moves_label.pack(side=tk.RIGHT, padx=10)

        pause_button = tk.Button(self.info_frame, text="Pause", command=self.__toggle_timer, font=("Helvetica", 16))
        pause_button.pack(side=tk.LEFT, padx=10)

        reset_button = tk.Button(self.info_frame, text="Restart", command=self.__restart_game, font=("Helvetica", 16))
        reset_button.pack(side=tk.RIGHT, padx=10)

        for row in range(self.__size):
            button_row = []
            for col in range(self.__size):
                button = tk.Button(self.board_frame, text="*", font=("Helvetica", 48),
                                   command=lambda r=row, c=col: self.__on_button_click(r, c))
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                button_row.append(button)
            self.buttons.append(button_row)

        for row in range(self.__size):
            self.board_frame.grid_rowconfigure(row, weight=1)
            self.board_frame.grid_columnconfigure(row, weight=1)


    def __on_button_click(self, row, col):
        """Handle button click events and reveal/hide cells based on matching."""
        cell = self.__board[row][col]

        if cell.founded or (self.__first_click and (row, col) == self.__first_click):
            return  
        
        if not self.__first_click:
            self.__first_click = (row, col)
            self.buttons[row][col].config(text=str(cell.value))
        elif not self.__second_click:
            self.__second_click = (row, col)
            self.buttons[row][col].config(text=str(cell.value))
            self.__disable_buttons()
            self.root.after(500, self.__check_match) 

    def __disable_buttons(self):
        """Disable all buttons (prevent further clicks) until the match check is complete."""
        for row in range(self.__size):
            for col in range(self.__size):
                if not self.__board[row][col].founded: 
                    self.buttons[row][col].config(state="disabled")

    def __enable_buttons(self):
        """Enable all buttons (allow clicks again)."""
        for row in range(self.__size):
            for col in range(self.__size):
                if not self.__board[row][col].founded:  
                    self.buttons[row][col].config(state="normal")

    def __check_match(self):
        """Check if two selected cells match."""
        (x1, y1), (x2, y2) = self.__first_click, self.__second_click
        cell1, cell2 = self.__board[x1][y1], self.__board[x2][y2]

        if cell1 == cell2:
            cell1.founded = cell2.founded = True
            self.__win_case -= 1
            if self.__check_win():
                messagebox.showinfo("Congratulations!", f"You've won in {self.move_count} moves and {self.timer_seconds} seconds!")
                self.root.quit()
        else:
            self.buttons[x1][y1].config(text="*")
            self.buttons[x2][y2].config(text="*")

        self.move_count += 1
        self.moves_label.config(text=f"Moves: {self.move_count}")

        self.__first_click = None
        self.__second_click = None
        self.__enable_buttons()

    def __check_win(self) -> bool:
        """Check if the player has matched all pairs."""
        return self.__win_case == 0
    
    def __start_timer(self):
        if self.timer_running:
            self.timer_seconds += 1
            self.timer_label.config(text=f"Time: {self.timer_seconds}")
            self.root.after(1000, self.__start_timer)

    def __toggle_timer(self):
        """Pause or resume the timer."""
        self.timer_running = not self.timer_running
        if self.timer_running:
            self.__start_timer()

    def __restart_game(self):
        """Restart the game with the same settings."""
        self.root.destroy()
        self.__init__()

    def __load_leaderboard(self):
        """Load leaderboard data from a file."""
        if os.path.exists(self.leaderboard_file):
            with open(self.leaderboard_file, 'r') as file:
                self.leaderboard = json.load(file)
        else:
            self.leaderboard = []
