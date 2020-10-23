import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from tkinter.ttk import *

#gui 1 when requesting for new link or view old recordings
class Application1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="""
        Welcome to Costco_Recorder made by Jason Hsu
        this program will record and analyze the costco
        item catagory you entered! Here are 3 ways to
        use this program:
        1. To create a fresh costco recording:
            Enter costco catagory link and press "Analyze"
        2. To look at old, analyzed costco_recorder file:
            Press "Analyze" directly
        3. To Combine new link with old analyzed files:
            Enter link, press "Analyze" and in the next
            page please go to menu on top left and select
            old file by pressing "Open"
            *this function is currently disabled*""")
        self.label.pack()
        """
        self.load = tk.Button(self)
        self.load["text"] = "Enter"
        self.load["command"] = self.pressed
        self.load.pack(side="right")
        """
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
        if self.contents.get() != "":
            return self.contents.get()
        else:
            return "readfile"
        
class runtk1:
    def callGUI():
        root = tk.Tk()
        app = Application1(master=root)
        app.master.title("Costco Recorder Start-up")
        root.geometry("350x260")
        app.mainloop()
        return app.getLink()

#for testing
#runtk1.callGUI()