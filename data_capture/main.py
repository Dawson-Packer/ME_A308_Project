from datetime import timedelta
import os
import signal
import sys
import time

from serial import Serial, SerialException
from serial.tools import list_ports

os.chdir(os.path.join(__file__))

ultrasonic_file = None
pressure_file = None
float_file = None

start_time = 0

ser: Serial | None = None

ultrasonic_data = []
pressure_data = []
float_data = []

def main():
    
    device_port = ''
    
    for comport in list_ports.comports():
        if comport.description.find("Arduino Uno") != -1:
            device_port = comport.name
    
    ser = Serial(port=device_port, baudrate=9600)
    try:
        ser.open()
    except SerialException as e:
        print(f"Failed to open port {device_port}: {e}")

    try:
        ultrasonic_file = open(os.path.join('.', 'ultrasonic_data.csv'), 'w')
    except OSError as e:
        print(e)
        return
    try:
        pressure_file = open(os.path.join('.', 'pressure_data.csv'), 'w')
    except OSError as e:
        print(e)
        return
    try:
        float_file = open(os.path.join('.', 'float_data.csv'), 'w')
    except OSError as e:
        print(e)
        return
    
    start_time = time.time()

    while True:
        result = bytes.decode(ser.readall())

        ultrasonic_reading = {
            'time': time.time() - start_time,
            'data': float(result.split('US: ')[1].split('P: ')[0]),
        }

        pressure_reading = {
            'time': time.time() - start_time,
            'data': float(result.split('P: ')[1].split('F: ')[0]),
        }

        float_reading = {
            'time': time.time() - start_time,
            'data': float(result.split('F: ')[1]),
        }

        ultrasonic_data.append(ultrasonic_reading)
        pressure_data.append(pressure_reading)
        float_data.append(float_reading)


def stop_collecting_data():
    
    ultrasonic_csv_data = '\n'.join([f"{x['time']},{x['data']}" for x in ultrasonic_data])
    pressure_csv_data = '\n'.join([f"{x['time']},{x['data']}" for x in pressure_data])
    float_csv_data = '\n'.join([f"{x['time']},{x['data']}" for x in float_data])

    ultrasonic_file.write(ultrasonic_csv_data)
    pressure_file.write(pressure_csv_data)
    float_file.write(float_csv_data)

    ultrasonic_file.close()
    pressure_file.close()
    float_file.close()

    if ser:
        ser.close()

if __name__ == '__main__':

    signal.signal(signal.SIGINT, stop_collecting_data)
    main()