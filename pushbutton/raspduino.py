import serial
import time

arduino = serial.Serial('/dev/ttyACM0', 9600)

while 1:
    # if(arduino.in_waiting > 0):
        x = arduino.readline()
        print x
        time.sleep(30)
        
arduino.close()
