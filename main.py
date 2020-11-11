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

        # temp chart values
        self.tempChar = None
        self.tempCharIndex = 1
        self.tempCharX = 50
        self.tempCharY = self.value_to_y(50)

        self.lightChar = None
        self.lightCharIndex = 1
        self.lightCharX = 50
        self.lightCharY = self.value_to_y(50)

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

    def createMainContent(self):
        """
        This method creates all the content of the main.

        :return:
        """
        self.createTempChart()
        self.createLightChart()
        self.main.grid(row=0, column=1, sticky="nsew")

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

    def createTempChart(self):
        """
        This method creates the temperature chart

        :return:
        """
        label_radio = tk.Label(self.main, text="Temperatuur")
        label_radio.pack()

        self.tempChar = tk.Canvas(self.main, width=1200, height=600)  # 0,0 is top left corner
        self.tempChar.pack(expand=tk.YES, fill=tk.BOTH)
        self.createTempChartAxis()

    def createTempChartAxis(self):
        """
        This methods creates the axis of the x and y ash of the temperature chart

        :return:
        """
        # x-axis
        for i in range(23):
            x = 50 + (i * 50)
            self.tempChar.create_line(x, 550, x, 50, width=1, dash=(2, 5))
            self.tempChar.create_text(x, 550, text='%d' % (10 * i), anchor=tk.N)

        # y-axis
        for i in range(11):
            y = 550 - (i * 50)
            self.tempChar.create_line(50, y, 1150, y, width=1, dash=(2, 5))
            self.tempChar.create_text(40, y, text='%d' % (10 * i), anchor=tk.E)

    def createLightChart(self):
        """
        This method creates the lightning chart

        :return:
        """
        label_radio = tk.Label(self.main, text="Lichtintensiteit")
        label_radio.pack()

        self.lightChar  = tk.Canvas(self.main, width=1200, height=600)  # 0,0 is top left corner
        self.lightChar.pack(expand=tk.YES, fill=tk.BOTH)
        self.createLightChartAxis()

    def createLightChartAxis(self):
        """
        This methods creates the axis of the x and y ash of the lightning chart

        :return:
        """
        # x-axis
        for i in range(23):
            x = 50 + (i * 50)
            self.lightChar.create_line(x, 550, x, 50, width=1, dash=(2, 5))
            self.lightChar.create_text(x, 550, text='%d' % (10 * i), anchor=tk.N)

        # y-axis
        for i in range(11):
            y = 550 - (i * 50)
            self.lightChar.create_line(50, y, 1150, y, width=1, dash=(2, 5))
            self.lightChar.create_text(40, y, text='%d' % (10 * i), anchor=tk.E)

    def save(self):
        """
        This method saves the values for the sunscreen

        :return:
        """
        print("Saved")
        # self.radioValue.get()

    def addTemp(self, temp):
        """
        This method will add a line to the temperature chart

        :param temp:
        :return:
        """
        if self.tempCharIndex == 23:
            self.tempCharIndex = 1
            self.tempCharX = 50
            self.tempChar.delete('temp')

        x1 = self.tempCharX
        y1 = self.tempCharY
        self.tempCharX = 50 + self.tempCharIndex * 50
        self.tempCharY = self.value_to_y(temp)

        self.tempChar.create_line(x1, y1, self.tempCharX, self.tempCharY, fill='blue', tags='temp')
        self.lightCharIndex += 1

    def addLight(self, light):
        """
        This method will add a line to the lightning chart

        :param light:
        :return:
        """
        if self.lightCharIndex == 23:
            self.lightCharIndex = 1
            self.lightCharX = 50
            self.lightChar.delete('temp')

        x1 = self.lightCharX
        y1 = self.lightCharY
        self.lightCharX = 50 + self.lightCharIndex * 50
        self.lightCharY = self.value_to_y(light)

        self.lightChar.create_line(x1, y1, self.lightCharX, self.lightCharY, fill='blue', tags='temp')
        self.lightCharIndex += 1

    def setTemp(self):
        """
        This method set the temperature lines form the arduino

        :return:
        """
        string = self.arduino.read()
        number = int.from_bytes(string, byteorder='big')
        self.addTemp(number)
        self.tempChar.after(300, self.setTemp)

    def setLight(self):
        """
        This method set the lightning lines form the arduino

        :return:
        """
        string = self.arduino.read()
        number = int.from_bytes(string, byteorder='big')
        self.addLight(number)
        self.lightChar.after(300, self.setLight)

    def value_to_y(self, val):
        """
        This method calculates the value of the y ash for the charts.

        :param val:
        :return:
        """

        return 550 - 5 * val
# Main
def main():
    window = tk.Tk()
    window.title("Sunshine")
    application = Application(window)
    application.mainloop()

main()

print("Closed")
