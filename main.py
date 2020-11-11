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
        
        def createSidebarContent(self):
            """
            This method creates all the content of the sidebar.

            :return:
            """
            self.createRadios()
            self.createSlides()
            self.createSave()

        self.sidebar.grid(row=0, column=0, sticky="ns")

    def createRadios(self):
        """
        This method creates the specific radios to select the status of the sunscreen.

        :return:
        """
        label_radio = tk.Label(self.sidebar, text="Zonnescherm")
        label_radio.pack()

        v = tk.IntVar()
        radiobutton_widget_on = tk.Radiobutton(self.sidebar, text="Aan", variable=v, value=1, justify='left')
        radiobutton_widget_off = tk.Radiobutton(self.sidebar, text="Uit", variable=v, value=2, justify='left')
        radiobutton_widget_system = tk.Radiobutton(self.sidebar, text="System", variable=v, value=3, justify='left')
        v.set(1)
        radiobutton_widget_on.pack()
        radiobutton_widget_off.pack()
        radiobutton_widget_system.pack()

    def createSlides(self):
        """
        This method creates the specific slides to select the maximum and the minimum of the value of the sunscreen.

        :return:
        """
        label_radio = tk.Label(self.sidebar, text="Minimale rolluit")
        label_radio.pack()

        scale_widget_min = tk.Scale(self.sidebar, from_=0, to=100, orient=tk.HORIZONTAL)
        scale_widget_min.set(25)
        scale_widget_min.pack()

        label_radio = tk.Label(self.sidebar, text="Maximale rolluit")
        label_radio.pack()

        scale_widget_max = tk.Scale(self.sidebar, from_=0, to=100, orient=tk.HORIZONTAL)
        scale_widget_max.set(25)
        scale_widget_max.pack()

    def createSave(self):
        button_hello = tk.Button(self.sidebar, text="save", command=self.save)
        button_hello.pack()

# Main
def main():
    window = tk.Tk()
    window.title("Sunshine")
    application = Application(window)
    application.mainloop()

main()

print("Closed")
