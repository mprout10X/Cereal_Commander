import serial

port = "COM13"
baud = 9600

ser = serial.Serial(port, baud, timeout=1)
# open the serial port
if ser.isOpen():
    print(ser.name + ' is open...')

while True:
    cmd = raw_input("Enter command or 'exit':")
    if cmd == 'exit':
        ser.close()
        exit()
    else:
        ser.write(cmd)
        out = ser.read()
        print(out)
