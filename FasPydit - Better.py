from tkinter import *;  from tkinter.filedialog import *
def savefile():
    with open(asksaveasfile(mode="w", defaultextension=".py").name, "w") as sf:
        sf.write(text.get("1.0", END))
def openfile():
    with open(askopenfilename(filetypes=[("Python Scripts", "*.py"), ("All Files", "*.*")]), "r") as of:
        text.delete(1.0, END)
        text.insert(1.0, of.read())
root = Tk()
root.title("FasPydit - Better")
save = Button(root, text="Save", command=savefile)
save.pack(fill="x")
ope = Button(root, text="Open", command=openfile)
ope.pack(fill="x")
text = Text(root, font=("Helvetica Bold", 16))
text.pack(fill="both",expand=True)
notepad = Entry(root, font=("Times", 14))
notepad.insert(0, "Notes:")
notepad.pack(fill="x")
root.mainloop()