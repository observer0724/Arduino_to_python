import serial
import time

ser = serial.Serial('/dev/ttyACM0')



for i in range(10000):
    data = ser.readline()
    t = time.time()

    print (data)
    print (',')
    print (t)
    time.sleep(0.001)
