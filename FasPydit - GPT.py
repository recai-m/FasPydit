from tkinter import *
from tkinter.filedialog import *
def open_file():
    path = askopenfilename()
    if path:
        with open(path, "r") as file:
            editor.delete(1.0, END)
            editor.insert(INSERT, file.read())
def save_file():
    path = asksaveasfilename()
    if path:
        with open(path, "w") as file:
            file.write(editor.get(1.0, END))
root = Tk()
root.title("FasPydit - GPT")
editor = Text(root)
editor.pack(fill=BOTH, expand=True)
Button(root, text="Open", command=open_file).pack(side=LEFT)
Button(root, text="Save", command=save_file).pack(side=LEFT)
root.mainloop()