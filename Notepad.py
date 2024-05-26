import tkinter as tk
from tkinter import filedialog


def newFile():
    global current_file
    text_info.delete("1.0", "end")
    root.title("New File")
    current_file = None

def openFile():
    global current_file
    text_info.delete("1.0", "end")
    
    text_file = filedialog.askopenfilename(initialdir="/Users/armanvossoughi/Desktop", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
   
    if text_file:
        current_file = text_file
        name = text_file.replace("/Users/armanvossoughi/Desktop", "")
        root.title(f'{name} - Notepad')
        
        with open(text_file, 'r') as file:
            stuff = file.read()
            text_info.insert("1.0", stuff)

def saveFile():
    global current_file
    if current_file:
        with open(current_file, 'w') as file:
            file.write(text_info.get("1.0", tk.END))
        name = current_file.replace("/Users/armanvossoughi/", "")
        root.title(f'{name} - Notepad')
    else:
        saveFileAs()

def saveFileAs():
    global current_file
    text_file = filedialog.asksaveasfilename(defaultextension=".txt", initialdir="/Users/armanvossoughi/", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if text_file:
        current_file = text_file
        with open(text_file, 'w') as file:
            file.write(text_info.get("1.0", tk.END))
        name = text_file.replace("/Users/armanvossoughi/", "")
        root.title(f'{name} - Notepad')

def cut_text(e):
    global selected
    if text_info.selection_get():
        selected = text_info.selection_get()
        text_info.delete("sel.first", "sel.last")

def paste_text(e):
    if selected:
        position = text_info.index("insert")
        text_info.insert(position, selected)

current_file = None

global selected
selected = False
root = tk.Tk()
root.title("Notepad")
root.geometry("600x600")
root.configure(bg="white")

my_frame = tk.Frame(root)
my_frame.pack(pady=5, expand=True, fill="both")

scrollbar = tk.Scrollbar(my_frame)
scrollbar.pack(side="right", fill="y")

text_info = tk.Text(my_frame,
                    font=("Helvetica", 16),
                    selectbackground="yellow",
                    selectforeground="black",
                    undo=True, 
                    yscrollcommand=scrollbar.set,
                    bg="white", 
                    fg="black", 
                    highlightbackground="white",
                    highlightcolor="white", 
                    highlightthickness=1, 
                    insertbackground="black")

text_info.pack(expand=True, fill="both")

scrollbar.config(command=text_info.yview)

my_menu = tk.Menu(root)
root.config(menu= my_menu)

file_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=newFile)
file_menu.add_command(label="Open", command=openFile)
file_menu.add_command(label="Save", command=saveFile)
file_menu.add_command(label="Save As...", command=saveFileAs)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)

edit_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command = lambda:cut_text(False))
edit_menu.add_command(label="Paste", command = lambda:paste_text(False))


root.mainloop()
