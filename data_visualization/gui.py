import customtkinter as ctk
import tkinter as tk
import serial

import time
import threading

import random
import re

import serial.tools
import serial.tools.list_ports
import plot

BG_COLOR = '#d9d9d9'
UPDATE_PERIOD = 0.5
DATA_PERIOD = 0.1

class TankLevelRegulatorGui:

    def __init__(self):
        self.app = ctk.CTk()
        self.app.title = "Tank Level Regulator Project - Spring 2025"
        self.app.columnconfigure(1, weight=1)
        self.app.rowconfigure(0, weight=1)

        self.ser = None
        for port in serial.tools.list_ports.comports():
            if port.description.find('Arduino Uno') != -1:
                self.ser = serial.Serial(port.name, baudrate=9600)
        

        self._scheduled_update_id = None
        self._scheduled_data_id = None
        self._is_running = True
        self.app.protocol('WM_DELETE_WINDOW', self.cleanup)

        ctk.set_appearance_mode("light")


        left_frame = ctk.CTkFrame(self.app, bg_color=BG_COLOR)
        left_frame.grid(row=0, column=0, padx=10, pady=5, sticky=tk.NSEW)
        right_frame = ctk.CTkFrame(self.app, bg_color=BG_COLOR)
        right_frame.grid(row=0, column=1, padx=10, pady=5, sticky=tk.NSEW)
        right_frame.grid_columnconfigure((0), weight=1)
        right_frame.grid_rowconfigure((0), weight=1)

        self._time = []
        self._float_data = []
        self._pressure_data = []
        self._ultrasonic_data = []

        self.plot = plot.Plot(right_frame)

    def get_data(self):
        
        while self._is_running:
            start_time = time.time()
            read_line = self.ser.read_until(b'\n').decode('utf-8')
            print(read_line)

            time_data = re.findall(r'T: \d+', read_line)[0]
            pressure_data: tuple[str] = re.findall(r'(P: \d+(\.\d+)?)', read_line)[0]
            float_data: tuple[str] = re.findall(r'(F: \d+(\.\d+)?)', read_line)[0]
            ultrasonic_data: tuple[str] = re.findall(r'(US: \d+(\.\d+)?)', read_line)[0]
            print(time_data, pressure_data, float_data, ultrasonic_data)

            self._time.append(float(time_data[3:])/(1e3))
            for entry in pressure_data:
                if entry.startswith('P'):
                    self._pressure_data.append(float(entry[3:]))
            for entry in float_data:
                if entry.startswith('F'):
                    self._float_data.append(float(entry[3:]))
            for entry in ultrasonic_data:
                if entry.startswith('US'):
                    self._ultrasonic_data.append(float(entry[4:]))
            
            while time.time() - start_time < DATA_PERIOD: pass

    def update_graphs(self):

        while self._is_running:
            start_time = time.time()
            self.plot.update_with_data(
                self._time, self._pressure_data, self._float_data,
                self._ultrasonic_data)
        
            while time.time() - start_time < UPDATE_PERIOD: pass

    @property
    def is_running(self): return self._is_running

    def cleanup(self):
        if self._scheduled_update_id:
            self.app.after_cancel(self._scheduled_update_id)
        if self._scheduled_data_id:
            self.app.after_cancel(self._scheduled_data_id)
        self._is_running = False
        self.app.quit()

    def start(self):
        self.data_thread = threading.Thread(target=self.get_data)
        self.data_thread.start()
        self.update_thread = threading.Thread(target=self.update_graphs)
        self.update_thread.start()
        self.app.mainloop()
    
    def add_data(self, time: float, pressure: float, float: float, ultrasonic: float):
        self._time.append(time)
        self._pressure_data.append(pressure)
        self._float_data.append(float)
        self._ultrasonic_data.append(ultrasonic)

        self._time = self._time[-1000:]
        self._float_data = self._float_data[-1000:]
        self._pressure_data = self._pressure_data[-1000:]
        self._ultrasonic_data = self._ultrasonic_data[-1000:]