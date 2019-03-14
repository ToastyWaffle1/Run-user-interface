from Tkinter import *
from os import *
from subprocess import *
import ttk
import os
import subprocess
import webbrowser
class Application(Frame):
    def Yeet(self):
        print('Cancer')
        url = 'https://www.reddit.com'
        webbrowser.open_new_tab(url + 'doc/')
        webbrowser.open_new(url)
    def SassyRetort(self):
        print("Good luck :")
        #url = "Desktop/Server/html/Projecto.html"
        #subprocess.call(
    #["/usr/bin/open", "-W", "-n", "-a", "/Applications/Safari.app"]
            #)
        #webbrowser.open('url, new=2')
        url = 'https://github.com/ToastyWaffle1'

# Open URL in a new tab, if a browser window is already open.
        webbrowser.open_new_tab(url + 'doc/')

# Open URL in new window, raising the window if possible.
        webbrowser.open_new(url)

    def Run2(self):
        print("Hi")
        subprocess.call(
    ["/usr/bin/open", "-W", "-n", "-a", "/Applications/Atom.app"]
    )
    def say_hi(self):
        print "Here is the launcher for an encryption software"
        print"Here are the terms of service"
        print"- All data collected here is secure"
    def Run(self):
        print"F-R-E-E THAT SPELLS FREE"
        #under is how to open an app on OSX, just replace chess with another app
        subprocess.call(
    ["/usr/bin/open", "-W", "-n", "-a", "/Applications/Chess.app"]
    )
        #def open_file(filename):
            #if sys.platform == "win32":
                #os.startfile("/Application/Chess.app")
            #else:
                #opener  ="open" if sys.platform == "darwin" else "xdg-open"
                #subprocess.call(["open Chess.app"])
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
        self.RUN["text"] = "RUN CHESS"
        self.RUN["command"] = self.Run

        self.RUN.pack({"side": "left"})

        self.TextEdit = Button(self)
        self.TextEdit["text"] = "RUN ATOM"
        self.TextEdit["command"] = self.Run2

        self.TextEdit.pack({"side": "left"})

        self.TextBox = Button(self)
        self.TextBox["text"] = "Open GitHub"
        self.TextBox["command"] = self.SassyRetort

        self.TextBox.pack({"side": "left"})

        self.reddit = Button(self)
        self.reddit["text"] = "Open Rediit"
        self.reddit["command"] = self.Yeet

        self.reddit.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
