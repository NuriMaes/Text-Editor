import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.current_file = None
        self.update_title()

        # 1. UI Layout
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side='top', fill='x')

        self.open_button = tk.Button(self.button_frame, text='Open', command=self.open_file)
        self.open_button.pack(side='left', padx=5, pady=5)

        self.save_button = tk.Button(self.button_frame, text='Save', command=self.save_file)
        self.save_button.pack(side='left', padx=5, pady=5)

        self.text_area = tk.Text(self.root)
        self.text_area.pack(expand=True, fill='both')

        # 2. Key Bindings (macOS style)
        self.save_event = self.root.bind("<Command-s>", self.save_file)
        self.open_event = self.root.bind("<Command-o>", self.open_file)
    
    def update_title(self):
        '''Updates the window title based on the current file path.'''
        title_prefix = 'Python Text Editor'
        if self.current_file:
            self.root.title(f'{title_prefix} - {self.current_file}')
        else:
            self.root.title(f'{title_prefix} - New File')

    def open_file(self, event=None):
        '''Opens a file and loads its content into the text area.'''
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

        if file_path:
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                self.current_file = file_path
                self.text_area.delete('1.0', tk.END)
                self.text_area.insert('1.0', content)
                self.update_title()
            except Exception as e:
                print(f'Error opening file: {e}')

    def save_file(self, event=None):
        '''Saves the current text area content to a file.'''
        # Case 1: New file, we need a path
        if not self.current_file:
            new_path = filedialog.asksaveasfilename(defaultextension=".txt")
            if not new_path:
                return # User cancelled
            self.current_file = new_path

        # Case 2: We have a path, just write the content
        try:
            # 'end-1c' avoids adding an extra newline at the end of the file
            content = self.text_area.get('1.0', 'end-1c')
            with open(self.current_file, 'w') as file:
                file.write(content)
            
            self.update_title()
            print(f"File saved: {self.current_file}")
        except Exception as e:
            print(f"Error saving file: {e}")

# Main execution
if __name__ == "__main__":
    main_window = tk.Tk()
    app = TextEditor(main_window)
    main_window.mainloop()
