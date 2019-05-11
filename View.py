import tkinter
from tkinter import *

class View(tkinter.Frame):
    """
    Class View is the VIEW for a simple program that contains three buttons,     two entry areas, and four labels:
    one button a converter;
    one button quits the program;
    one button clears the program;
    one entry is for celsius;
    one entry is for fahrenheit;
    and the labels prompt user for input, and label the entry values as needed.
    """
    def __init__(self, controller):
        """
        places the controls on the frame
        """
        tkinter.Frame.__init__(self) #initilizes the superclass
        self.pack()  # required for the buttons to show up properly.
        self.controller = controller  # saves ref to controller to call methods on
        # contoller object when user generates events

        #Button to get a random song
        self.randomize =tkinter.Label(self)
        self.randomize["text"] ="Random song"
        self.randomize.grid(row=0, column = 1)

        self.randomizeButton =tkinter.Button(self)
        self.randomizeButton["text"] = "Randomize"
        self.randomizeButton["command"] = self.controller.buttonPressed
        self.randomizeButton.grid(row=1, column=1)

        #print song
        self.songText = tkinter.Label(self)
        self.songText.grid(row=2, column=1)

        #song name
        self.title = tkinter.Label(self)
        self.title["text"] = "Name"
        self.title.grid(row=3, column=1)

        # print song name
        self.songName = tkinter.Label(self)
        self.songName.grid(row=4, column=1)

        # artist name
        self.artistTitle = tkinter.Label(self)
        self.artistTitle["text"] = "Artist"
        self.artistTitle.grid(row=3, column=2)

        # print artist name
        self.artist = tkinter.Label(self)
        self.artist.grid(row=4, column=2)

        # level
        self.levelText = tkinter.Label(self)
        self.levelText["text"] = "Level"
        self.levelText.grid(row=3, column=4)

        # print level
        self.level = tkinter.Label(self)
        self.level.grid(row=4, column=4)

        # mode
        self.modeText = tkinter.Label(self)
        self.modeText["text"] = "Mode"
        self.modeText.grid(row=3, column=6)

        # print mode
        self.mode = tkinter.Label(self)
        self.mode.grid(row=4, column=6)

        #quit button
        self.quitButton = tkinter.Button(self)
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] = self.quit
        self.quitButton.grid(row=8, column=1)