import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()
"""
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
"""
