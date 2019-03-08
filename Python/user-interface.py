from Tkinter import *
from os import *
from subprocess import *
import ttk
import os
import subprocess
class Application(Frame):
    def say_hi(self):
        print "Here is the launcher for an encryption software"
        print"Here are the terms of service"
        print"- All data collected here is secure"
    def Run(self):
        def open_file(filename):
            if sys.platform == "win32":
                os.startfile("/Application/Chess.app")
            else:
                opener  ="open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call(["opener Chess.app"])
        #subprocess.run(["open ", "-a" "/Application/Chess.app"])




    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

        self.RUN = Button(self)
        self.RUN["text"] = "RUN"
        self.RUN["command"] = self.Run

        self.RUN.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
