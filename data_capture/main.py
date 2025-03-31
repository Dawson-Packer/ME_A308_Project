import os
import time

from serial import Serial
from serial.tools import list_ports

os.chdir(os.path.dirname(__file__))

ultrasonic_file = open(os.path.join('.', 'ultrasonic_data.csv'), 'w')
pressure_file = open(os.path.join('.', 'pressure_data.csv'), 'w')
float_file = open(os.path.join('.', 'float_data.csv'), 'w')

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
    
    start_time = time.time()

    while True:
        result = bytes.decode(ser.read_until(b'\n'))

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

        print("Read: ____________________")
        print(f"Ultrasonic: {ultrasonic_reading['data']} us")
        print(f"Pressure  : {pressure_reading['data']} V")
        print(f"Float     : {float_reading['data']} V")
        print("")

        ultrasonic_data.append(ultrasonic_reading)
        pressure_data.append(pressure_reading)
        float_data.append(float_reading)


def stop_collecting_data():
    print("Saving data...")
    
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

    try:
        main()
    except KeyboardInterrupt:
        stop_collecting_data()