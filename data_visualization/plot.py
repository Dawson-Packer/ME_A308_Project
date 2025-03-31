from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk

BG_COLOR = '#d9d9d9'
LINE_COLOR = '#1e1e1e'

class Plot(FigureCanvasTkAgg):

    def __init__(self, master):
        self.figure = plt.figure(layout='constrained', figsize=(4,3))
        super().__init__(self.figure, master=master)

        self.figure.set_facecolor(BG_COLOR)
        self.subplot = self.figure.add_subplot(1, 1, 1)
        self.subplot.set_facecolor(BG_COLOR)

        for side in ['bottom', 'top', 'right', 'left']:
            self.subplot.spines[side].set_color(LINE_COLOR)
        for axis in ['x', 'y']:
            self.subplot.tick_params(axis=axis, colors=LINE_COLOR)

        plt.rc('font', **{'size': 10})
        plt.rcParams.update({'text.color': LINE_COLOR, 'axes.labelcolor': LINE_COLOR})
    
    def update_with_data(self, time: list[float], pressure: list[float], float: list[float], ultrasonic: list[float]):
        self.subplot.clear()

        self.subplot.plot(time, pressure, label="Pressure Sensor Voltage (V)", linestyle='-')
        self.subplot.plot(time, float, label="Float Potentiometer Voltage (V)", linestyle='-')
        self.subplot.plot(time, ultrasonic, label="Ultrasonic Time (s)", linestyle='-')

        plt.legend()
        plt.xlabel("Time (s)")
        plt.ylabel("Tank Height (mm — CHANGE)")

        self.draw()
        self.get_tk_widget().grid(row=0, column=0, sticky=tk.NSEW)