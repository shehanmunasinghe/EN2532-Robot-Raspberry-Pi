import serial

ser = serial.Serial('/dev/ttyS0') 

while True:
    line = ser.readline()
    print(str(line))

ser.close() 

print(ser.name)      