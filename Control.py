import tkinter
import Model
import View

class Controller:
    """
    The controller is the Controller for an app that follows the Model/View/Controller architecture.
    When the user presses a Button on the View,
    The Controller handles all communication between the Model and the View.
    """
    def __init__(self):
        root = tkinter.Tk()
        self.model =  Model.Model()
        self.view = View.View(self)
        self.view.mainloop()
        root.destroy()

    def buttonPressed(self):
        self.model.random()
        self.view.songName["text"] = self.model.songName()
        self.view.artist["text"] = self.model.artistName()
        self.view.level["text"] = self.model.level()
        self.view.mode["text"] = self.model.mode()


c = Controller()