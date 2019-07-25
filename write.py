import serial

ser = serial.Serial('/dev/ttyS0',9600,timeout=1) 


while True:
    print("ser.write")
    ser.write((b'B'))	#.encode(encoding="ascii"))
        


ser.close() 

print(ser.name)      
