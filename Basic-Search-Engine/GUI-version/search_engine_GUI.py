import os
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import search_engine as se

class SearchEngineGUI:
    PADDING_X = 60
    PADDING_Y = 20
    BUTTON_WIDTH = 15
    FONT_SIZE_LABEL = 26
    FONT_SIZE_BUTTON = 18
    FONT_SIZE_ENTRY = 18
    FONT_SIZE_RESULTS = 18

    def __init__(self, root):
        self.root = root
        self.root.title("Basic Search Engine")
        self.root.attributes('-fullscreen', True)  
        self.root.bind("<Escape>", self.toggle_fullscreen)  
        self.search_engine = se.BasicSearchEngine()
        self.folder_path = ""
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("Custom.TLabelframe.Label", font=("Arial", self.FONT_SIZE_LABEL)) 
        style.configure("Custom.TButton", font=("Arial", self.FONT_SIZE_BUTTON), padding=10)
        style.configure("Custom.TLabel", font=("Arial", self.FONT_SIZE_ENTRY))
        style.configure("Custom.TEntry", font=("Arial", self.FONT_SIZE_ENTRY))

        index_frame = ttk.LabelFrame(self.root, text="Indexing", style="Custom.TLabelframe")
        index_frame.pack(fill="x", padx=self.PADDING_X, pady=self.PADDING_Y)
        
        self.index_button = ttk.Button(
            index_frame, 
            text="Index Web Pages", 
            command=self.index_web_pages,
            style="Custom.TButton",
            width=self.BUTTON_WIDTH
        )
        self.index_button.pack(padx=20, pady=self.PADDING_Y)

        search_frame = ttk.LabelFrame(self.root, text="Search", style="Custom.TLabelframe")
        search_frame.pack(fill="x", padx=self.PADDING_X, pady=self.PADDING_Y)
        
        self.search_label = ttk.Label(search_frame, text="Enter Search Query:", style="Custom.TLabel")
        self.search_label.pack(side=tk.LEFT, padx=20, pady=self.PADDING_Y)

        self.search_entry = ttk.Entry(search_frame, width=50, style="Custom.TEntry")
        self.search_entry.pack(side=tk.LEFT, padx=20, pady=self.PADDING_Y)

        self.search_button = ttk.Button(
            search_frame, 
            text="Search", 
            command=self.perform_search,
            style="Custom.TButton",
            width=self.BUTTON_WIDTH
        )
        self.search_button.pack(side=tk.LEFT, padx=20, pady=self.PADDING_Y)

        results_frame = ttk.LabelFrame(self.root, text="Search Results", style="Custom.TLabelframe")
        results_frame.pack(fill="x", expand=True, padx=self.PADDING_X, pady=self.PADDING_Y)

        self.results_text = scrolledtext.ScrolledText(
            results_frame, 
            wrap=tk.WORD, 
            state='disabled', 
            font=("Arial", self.FONT_SIZE_RESULTS),
            height=15
        )
        self.results_text.pack(fill="both", padx=60, pady=self.PADDING_Y)  

        view_frame = ttk.LabelFrame(self.root, text="View File Content", style="Custom.TLabelframe")
        view_frame.pack(fill="x", padx=self.PADDING_X, pady=self.PADDING_Y)

        self.view_button = ttk.Button(
            view_frame, 
            text="View File", 
            command=self.view_file_content, 
            style="Custom.TButton", 
            width=self.BUTTON_WIDTH,
            state='disabled'
        )
        self.view_button.pack(padx=20, pady=self.PADDING_Y)

        self.status = ttk.Label(self.root, text="Welcome to the Basic Search Engine!", relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)
        self.result_message_frame = None

    def toggle_fullscreen(self, event=None):
        """Toggle fullscreen mode."""
        current_state = self.root.attributes('-fullscreen')
        self.root.attributes('-fullscreen', not current_state)

    def index_web_pages(self):
        folder_selected = filedialog.askdirectory(title="Select Folder to Index")
        if folder_selected:
            self.folder_path = folder_selected
            if self.result_message_frame:
                self.result_message_frame.destroy()  
            
            self.result_message_frame = tk.Frame(self.root)
            self.result_message_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER) 
            
            result_label = ttk.Label(
                self.result_message_frame, 
                text=f"Indexing files in '{self.folder_path}'...", 
                font=("Arial", self.FONT_SIZE_LABEL)
            )
            result_label.pack(padx=25, pady=25)
            self.root.update_idletasks() 
            try:
                self.search_engine.index_files(self.folder_path)
                indexed_file_count = len(self.search_engine.indexed_files)  
                result_label.config(text=f"Successfully indexed {indexed_file_count} files.")
                self.view_button.config(state='normal')  
            except Exception as e:
                result_label.config(text=f"An error occurred: {str(e)}")
            close_button = ttk.Button(
                self.result_message_frame, 
                text="Close", 
                command=self.close_result_message
            )
            close_button.pack(pady=10)

    def close_result_message(self):
        """Close the result message frame."""
        if self.result_message_frame:
            self.result_message_frame.destroy()
            self.result_message_frame = None

    def perform_search(self):
        query = self.search_entry.get().strip()
        if not query:
            messagebox.showwarning("Input Error", "Please enter a search query.")
            return

        self.status.config(text=f"Searching for '{query}'...")
        self.root.update_idletasks()

        results = self.search_engine.search(query)
        self.display_search_results(results, query)

        self.status.config(text=f"Search completed for '{query}'.")

    def display_search_results(self, sorted_results: dict, query: str):
        self.results_text.config(state='normal')
        self.results_text.delete(1.0, tk.END)
        missing_words = [word for word in query.split() if word not in sorted_results]
        if missing_words:
            for word in missing_words:
                self.results_text.insert(tk.END, f"No results found for '{word}'.\n")
        for word, word_info_list in sorted_results.items():
            self.results_text.insert(tk.END, f"\nSearch results for '{word}':\n\n")
            for wi in word_info_list:
                self.results_text.insert(tk.END, f"{wi}\n")
        self.results_text.config(state='disabled')

    def view_file_content(self):
        """
        Opens a dialog to select an indexed file and displays its content.
        """
        if not self.search_engine.indexed_files:
            messagebox.showwarning("No Indexed Files", "Please index files first.")
            return

        view_window = tk.Toplevel(self.root)
        view_window.title("Select File to View")
        view_window.geometry("400x300")
        view_window.grab_set()  

        label = ttk.Label(view_window, text="Select a file to view:", style="Custom.TLabel")
        label.pack(pady=10)

        list_frame = ttk.Frame(view_window)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set, font=("Arial", self.FONT_SIZE_RESULTS))
        indexed_files = sorted(self.search_engine.indexed_files) 
        for file_path in indexed_files:
            display_name = os.path.basename(file_path)
            listbox.insert(tk.END, display_name)
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=listbox.yview)

        def on_view():
            selected_indices = listbox.curselection()
            if not selected_indices:
                messagebox.showwarning("No Selection", "Please select a file to view.")
                return
            selected_file_display = listbox.get(selected_indices[0])
            selected_file_full_path = next(
                (f for f in indexed_files if os.path.basename(f) == selected_file_display), None
            )
            if not selected_file_full_path:
                messagebox.showerror("Error", "Selected file not found.")
                return
            try:
                content = self.search_engine.get_file_content(selected_file_full_path)
                self.show_file_content(selected_file_display, content)
                view_window.destroy()  
            except Exception as e:
                messagebox.showerror("Error", str(e))

        buttons_frame = ttk.Frame(view_window)
        buttons_frame.pack(pady=10)

        view_btn = ttk.Button(buttons_frame, text="View", command=on_view, width=10)
        view_btn.pack(side=tk.LEFT, padx=5)

        close_btn = ttk.Button(buttons_frame, text="Close", command=view_window.destroy, width=10)
        close_btn.pack(side=tk.LEFT, padx=5)

    def show_file_content(self, file_name, content):
        """
        Displays the content of the selected file in the scrolled text widget.
        """
        self.results_text.config(state='normal') 
        self.results_text.delete(1.0, tk.END)  
        self.results_text.insert(tk.END, f"--- Content of '{file_name}' ---\n\n")
        self.results_text.insert(tk.END, content)
        self.results_text.insert(tk.END, "\n--- End of File ---")
        self.results_text.config(state='disabled')  

