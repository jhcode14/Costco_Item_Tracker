import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to Costco_Recorder made by Jason Hsu\nplease enter a costco catagory link that you would\nlike to record and be analyzed for you!")
        self.label.pack()

        self.load = tk.Button(self)
        self.load["text"] = "Enter"
        self.load["command"] = self.pressed
        self.load.pack(side="right")

        self.contents = tk.StringVar()
        self.entry = tk.Entry(self)
        self.entry.pack(side="left")
        self.entry["textvariable"] = self.contents

        self.quit = tk.Button(self, text="Analyze", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def pressed(self):
        if self.contents.get() != "":
            print ("you have entered:", self.contents.get(), "\nPress Analyze to continue")
        else:
            print("please enter a costco website catagory")
    def getLink(self):
        return self.contents.get()

class runtk:
    def callGUI():
        root = tk.Tk()
        app = Application(master=root)
        app.master.title("Costco Recorder")
        app.mainloop()
        return app.getLink()