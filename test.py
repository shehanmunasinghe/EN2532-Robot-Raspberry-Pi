import serial

ser = serial.Serial('/dev/ttyS0',timeout=1) 

while True:
    line = ser.readline()
    print(str(line).strip())

ser.close() 

print(ser.name)      