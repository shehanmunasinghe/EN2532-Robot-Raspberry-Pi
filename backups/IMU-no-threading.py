import serial
import os
import threading
import socket
import select


class IMU:
    def __init__(self):
        self.socket_in_ahrs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket_in_ahrs.bind(("0.0.0.0", 7000))

    def getEuler(self):
        ready = select.select([self.socket_in_ahrs], [], [], 0.025)
        #if ready[0]:
        try:
            data = self.socket_in_ahrs.recv(80).split()
            #print(data)

            if len(data) >= 4:
                roll = float(data[0])
                pitch = float(data[1])
                yaw = float(data[2])
                #frequency = str(data[3])

                return  roll, pitch, yaw 
            else:
                return 0,0,0
        except:
            
            #print("IMU Error")
            return 0,0,0


if __name__ == "__main__":
    print("This process has the PID", os.getpid())
    imu=IMU()
    while True:
        print(imu.getEuler())

