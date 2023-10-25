from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
    elif text == "C":
        scvalue.set("")
        screen.update
    else:
        scvalue.set(scvalue.get() + text)

root = Tk()
root.geometry("644x900")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

button_list = [
    "789",
    "456",
    "123",
    "0-*/",
    "%=+C"
]

for btn_row in button_list:
    f = Frame(root, background="grey")
    for char in btn_row:
        b = Button(f, text=char, padx=12, pady=8, font="lucida 35 bold")
        b.pack(side=LEFT, padx=8, pady=6)
        b.bind("<Button-1>", click)
    f.pack(pady=3)

root.mainloop()