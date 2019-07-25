import serial

ser = serial.Serial('/dev/ttyS0') 

print(ser.name)      