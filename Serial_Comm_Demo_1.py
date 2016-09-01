import time
import serial

# configure the serial connections
ser = serial.Serial(
    port='COM6',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

# ser.open()
ser.isOpen()

print 'Enter your commands below.\r\nInsert "exit" to leave the application.'

input = 1
while 1:
    # get keyboard input
    input = raw_input(">> ")
    if input == 'exit':
        ser.close()
        exit()
    else:
        # send the character to the device
        ser.write(input + '\r\n')
        out = ''
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1)

        if out != '':
            print ">>" + out
