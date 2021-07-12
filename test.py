#!/usr/bin/python3
import serial
import time
serial_port = serial.Serial(
    port="/dev/ttyS0",
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)
# Wait a second to let the port initialize
time.sleep(1)
try:
    while True:
        if serial_port.inWaiting() > 0:
            data = serial_port.readline()
            a=data[0:5]
            a=str(a,'utf-8')
            print(a)
except KeyboardInterrupt:
    print("Exiting Program")
except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))
finally:
    serial_port.close()
    pass