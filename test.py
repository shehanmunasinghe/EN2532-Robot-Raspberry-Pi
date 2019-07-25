import serial
import time

ser = serial.Serial('/dev/ttyS0',timeout=1) 

while True:
    line = ser.readline().decode().strip()
    print(line)
    if line=='DETECT':
        time.sleep(5)
        print("ser.write")
        ser.write((b'G'))

ser.close() 

print(ser.name)      