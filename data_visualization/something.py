import customtkinter as ctk
import tkinter as tk
import serial

import time
import threading
import math

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

        self.show_lifetime = False

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
        self.clear_btn = ctk.CTkButton(master=left_frame, width=80, height=28, corner_radius=3, text="Clear Graph", command=self.clear_graph)
        self.clear_btn.pack()

        self.lifetime_btn = ctk.CTkRadioButton(master=left_frame, width=80, height=28, corner_radius=3, text="Show Lifetime", command=self.toggle_lifetime)
        self.lifetime_btn.pack()

        right_frame = ctk.CTkFrame(self.app, bg_color=BG_COLOR)
        right_frame.grid(row=0, column=1, padx=10, pady=5, sticky=tk.NSEW)
        right_frame.grid_columnconfigure((0), weight=1)
        right_frame.grid_rowconfigure((0), weight=1)

        self._time = []
        self._float_data = []
        self._pressure_data = []
        self._ultrasonic_data = []
        self._float_angle = []

        self._time_lifetime = []
        self._float_data_lifetime = []
        self._pressure_data_lifetime = []
        self._ultrasonic_data_lifetime = []
        self._float_angle_lifetime = []



        self._float_3_readings = []
        self._pressure_3_readings = []
        self._ultrasonic_readings = []

        self.plot = plot.Plot(right_frame)

    def clear_graph(self):
        self._time = []
        self._float_data = []
        self._pressure_data = []
        self._ultrasonic_data = []
        self._time_lifetime = []
        self._float_data_lifetime = []
        self._pressure_data_lifetime = []
        self._ultrasonic_data_lifetime = []
        self._float_angle = []
        self._float_angle_lifetime = []


    def toggle_lifetime(self):
        self.show_lifetime = not self.show_lifetime
        if not self.show_lifetime:
            self.lifetime_btn.deselect()

    def get_data(self):
        
        while self._is_running:
            start_time = time.time()
            read_line = self.ser.read_until(b'\n').decode('utf-8')
            # print(read_line)
            try:
                time_data = re.findall(r'T: \d+', read_line)[0]
                pressure_data: tuple[str] = re.findall(r'(P: \d+(\.\d+)?)', read_line)[0]
                float_data: tuple[str] = re.findall(r'(F: \d+(\.\d+)?)', read_line)[0]
                ultrasonic_data: tuple[str] = re.findall(r'(US: \d+(\.\d+)?)', read_line)[0]
                # print(time_data, pressure_data, float_data, ultrasonic_data)
            except IndexError:
                continue
            time_seconds = 0
            pressure_voltage = 0
            float_voltage = 0
            ultrasonic_microseconds = 0
            time_seconds = float(time_data[3:])
            for entry in pressure_data:
                if entry.startswith('P'):
                    pressure_voltage = float(entry[3:])
            for entry in float_data:
                if entry.startswith('F'):
                    float_voltage = float(entry[3:])
            for entry in ultrasonic_data:
                if entry.startswith('US'):
                    ultrasonic_microseconds = float(entry[4:])
            
            self.add_data(time_seconds, pressure_voltage, float_voltage, ultrasonic_microseconds)
            
            while time.time() - start_time < DATA_PERIOD: pass

    def update_graphs(self):

        while self._is_running:
            start_time = time.time()
            if self.show_lifetime:
                self.plot.update_with_data(
                    self._time_lifetime, self._pressure_data_lifetime,
                    self._float_data_lifetime, self._ultrasonic_data_lifetime, self._float_angle_lifetime
                )
            else:
                self.plot.update_with_data(
                    self._time, self._pressure_data, self._float_data,
                    self._ultrasonic_data, self._float_angle)
        
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
    
    def add_data(self, time: float, pressure_voltage: float, float_voltage: float, ultrasonic_us: float):
        """
        Params
         pressure: float :: Pressure in Volts.
         float: float :: Potentiometer reading in Volts.
         ultrasonic: float :: Time to reflect in microseconds.
        
        """

#——Pressure Transducer——————————————————————————————————————————————————————————————————————————————

        P = 144.0*((pressure_voltage - 0.5)*5/(5.0-0.5)) # psf
        rho = 1.94 # slugs/ft^3
        g = 32.2 # ft/s^2
        p_height = (P / (rho*g)) * 12.0 # inches height h = P/(pg)

#——Potentiometer————————————————————————————————————————————————————————————————————————————————————

        H = 3.75 # in
        L = 3.5 # in
        R = 0.8125 # in
        H_W = 0.5 # in

        V_0 = 0.04395 # V
        V_1 = 0.10742 # V

        # voltage_percent = (float_voltage - V_0) / (V_1 - V_0)
        # if voltage_percent < 0: voltage_percent = 0.0

        theta_0 = 20 # degrees
        theta_1 = None # degrees

        theta = 35*float_voltage / 3.3 # degrees
        theta -= theta_0

        f_height = H - (L*math.sin(math.radians(theta)) + R) # in

#——Ultrasonic———————————————————————————————————————————————————————————————————————————————————————

        c = 1125.32808 # ft/s
        us_height = ((H/12) - c*((ultrasonic_us*1e-6)/2)) * 12.0 # in

        print(f"Height (in): Pressure: {p_height} in, Float: {f_height} in, Ultrasonic: {us_height} in")

        self._time.append(time * (1e-6))
        self._pressure_data.append(p_height)
        self._float_data.append(f_height)
        self._ultrasonic_data.append(us_height)
        self._time_lifetime.append(time * (1e-6))
        self._pressure_data_lifetime.append(p_height)
        self._float_data_lifetime.append(f_height)
        self._ultrasonic_data_lifetime.append(us_height)
        self._float_angle.append(360*float_voltage)
        self._float_angle_lifetime.append(360*float_voltage)

        self._time = self._time[-20:]
        self._float_data = self._float_data[-20:]
        self._pressure_data = self._pressure_data[-20:]
        self._ultrasonic_data = self._ultrasonic_data[-20:]