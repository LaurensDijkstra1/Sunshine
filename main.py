import tkinter as tk
import serial

class Application(tk.Frame):
    """
    The class that create the whole Sunshine application.
    """

    def __init__(self, window):
        """
        The initialization of the Sunshine application.

        :param window:
        """
        super().__init__(window)  # constructor frame

        # arduino
        # self.arduino = serial.Serial('COM3', 19200)

        # sidebar
        self.sidebar = tk.Frame(self, relief=tk.RAISED, bd=2)
        self.createSidebarContent()
        self.radioValue = tk.StringVar()

        # main
        self.main = tk.Frame(self, relief=tk.RAISED, bd=2)
        self.createMainContent()
        # self.setTemp()

        self.pack()
