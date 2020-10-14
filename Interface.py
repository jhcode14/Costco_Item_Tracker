import tkinter as tk

def change(entry):
    print(entry.widget.get())

window = tk.Tk()

label = tk.Label(
    text = "write something here and press enter(return)",
    bg="#34A2FE",
    width = 40,
    height = 20
)

button = tk.Button(
    text="ee",
    width = 40,
    height = 20,
    bg = "black",
    fg = "white"
)

#can use for HTTP link request
entry = tk.Entry(window
    #fg="black",
    #bg="white"
)

label.pack()
button.pack()
entry.pack()
entry.bind("<Return>", change)
window.mainloop()

