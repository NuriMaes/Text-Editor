import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Text Editor")
        self.root.geometry("600x400")

        # 1. First, we create and pack the button frame (The container)
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side='top', fill='x')

        # 2. We add buttons to that frame
        self.open_button = tk.Button(self.button_frame, text='Open', command=self.open_file)
        self.open_button.pack(side='left', padx=5, pady=5)

        self.save_button = tk.Button(self.button_frame, text='Save', command=self.save_file)
        self.save_button.pack(side='left', padx=5, pady=5)

        # 3. We create the text area to fill the remaining space
        self.text_area = tk.Text(self.root)
        self.text_area.pack(expand=True, fill='both')

        self.current_file = None
    
    def open_file(self):
        # 1. Ask for the file path
        file_path = filedialog.askopenfilename()

        # 2. Check if the user selected a file
        if file_path:

        # 3. Open the file in read mode ('r')
            with open(file_path, 'r') as file:
                # 4. Read the content
                content = file.read()
            self.current_file = file_path
            # 5. Delete current text in the widget
            self.text_area.delete('1.0', tk.END)
            # 6. Insert the new content
            self.text_area.insert('1.0', content)
        pass

    def save_file(self):

        if not self.current_file:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt")
            if file_path:
                self.current_file = file_path
            else:
                # User cancelled the dialog, so we stop here
                return

        # Once we have a path (either existing or new), we write the content
        try:
            content = self.text_area.get('1.0', tk.END)
            with open(self.current_file, 'w') as file:
                file.write(content)
            print(f"Successfully saved to: {self.current_file}")
        except Exception as e:
            print(f"An error occurred while saving: {e}")



# Main execution
main_window = tk.Tk()
app = TextEditor(main_window)

main_window.mainloop()
