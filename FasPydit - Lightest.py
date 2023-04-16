from tkinter import*;from tkinter.filedialog import*
def sa():
    with open(asksaveasfile().name,"w")as sf:
        sf.write(t.get("1.0",END))
def op():
    with open(askopenfilename(),"r")as of:
        t.delete(1.0,END)
        t.insert(1.0,of.read())
r=Tk()
s = Button(r,command=sa)
s.pack()
t = Text(r)
t.pack()
o = Button(r,command=op)
o.pack()
r.mainloop()