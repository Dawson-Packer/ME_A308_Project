from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk

BG_COLOR = '#d9d9d9'
LINE_COLOR = '#1e1e1e'

class Plot(FigureCanvasTkAgg):

    def __init__(self, master):
        self.figure = plt.figure(layout='constrained', figsize=(4,3))
        super().__init__(self.figure, master=master)

        self.time_recents = []
        self.pressure_recents = []
        self.float_recents = []
        self.time_history = []
        self.pressure_history = []
        self.float_history = []
        

        self.figure.set_facecolor(BG_COLOR)
        self.subplot = self.figure.add_subplot(1, 1, 1)
        self.subplot.set_facecolor(BG_COLOR)

        for side in ['bottom', 'top', 'right', 'left']:
            self.subplot.spines[side].set_color(LINE_COLOR)
        for axis in ['x', 'y']:
            self.subplot.tick_params(axis=axis, colors=LINE_COLOR)

        plt.rc('font', **{'size': 10})
        plt.rcParams.update({'text.color': LINE_COLOR, 'axes.labelcolor': LINE_COLOR})
    
    def update_with_data(self, time: list[float], pressure: list[float], float: list[float]):
        self.subplot.clear()

        if len(pressure) == 0: return

        if len(self.pressure_recents) < 2:
            print(len(self.pressure_recents))
            self.time_recents.append(time[-1])
            self.pressure_recents.append(pressure[-1])
            self.float_recents.append(float[-1])
            return
        average = lambda l: sum(l)/len(l) if len(l) > 0 else 0
        self.time_recents.append(time[-1])
        self.pressure_recents.append(pressure[-1])
        self.float_recents.append(float[-1])
        self.time_history.append(average(self.time_recents))
        self.pressure_history.append(average(self.pressure_recents))
        self.float_history.append(average(self.float_recents))



        self.subplot.plot(self.time_history, self.pressure_history, label="Pressure Sensor Height (in)", linestyle='-')
        self.subplot.plot(self.time_history, self.float_history, label="Float Potentiometer Height (in)", linestyle='-')
        # self.subplot.plot(time, ultrasonic, label="Ultrasonic Height (in)", linestyle='-')
        self.time_recents.clear()
        self.pressure_recents.clear()
        self.float_recents.clear()

        plt.legend()
        plt.xlabel("Time (s)")
        plt.ylabel("Tank Height (in)")

        self.draw()
        self.get_tk_widget().grid(row=0, column=0, sticky=tk.NSEW)