from serial.tools import list_ports

def main():
    
    device_port = ''
    
    for comport in list_ports.comports():
        if comport.description.find("Arduino Uno") != -1:
            device_port = comport.name
    
    if not device_port:
        print("Arduino not connected!")
        return
    
    print(f"Arduino connected to port {device_port}")
    
    cmd = f"arduino-cli upload -p {device_port} --fqbn arduino:avr:uno --verbose ./source/source.ino"
         
    with open('./scripts/upload.ps1', 'w') as stream:
        stream.write(cmd)
    
if __name__ == '__main__':
    main()