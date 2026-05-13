import tkinter as tk

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Text Editor")
        self.root.geometry("600x400")

        # 1. First, we create and pack the button frame (The container)
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side='top', fill='x')

        # 2. We add buttons to that frame
        self.open_button = tk.Button(self.button_frame, text='Open')
        self.open_button.pack(side='left', padx=5, pady=5)

        self.save_button = tk.Button(self.button_frame, text='Save')
        self.save_button.pack(side='left', padx=5, pady=5)

        # 3. LASTLY, we create the text area to fill the remaining space
        self.text_area = tk.Text(self.root)
        self.text_area.pack(expand=True, fill='both')

# Main execution
main_window = tk.Tk()
app = TextEditor(main_window)

main_window.mainloop()
