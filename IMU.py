import serial
import os
import threading
import socket
import select

import time


class IMU(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.socket_in_ahrs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket_in_ahrs.bind(("0.0.0.0", 7000))

        self.roll=0
        self.pitch=0
        self.yaw=0

    def run(self):
        while True:
            try:
                #ready = select.select([self.socket_in_ahrs], [], [], 0.025)
                #if ready[0]:
                #try:
                data = self.socket_in_ahrs.recv(80).split()
                #print(data)

                if len(data) >= 4:
                    self.roll = float(data[0])
                    self.pitch = float(data[1])
                    self.yaw = float(data[2])
                    #frequency = str(data[3])

                    #print( "%f %f %f" %(self.roll,self.pitch,self.yaw))
            except KeyboardInterrupt:
                exit()
                
    def getEuler(self):
        return self.roll, self.pitch, self.yaw

if __name__ == "__main__":
    print("This process has the PID", os.getpid())

    imu=IMU()
    imu.start()
    # while True:
    #     print(imu.getEuler())
    while True:
        print("Main")
        roll,pitch,yaw = imu.getEuler()
        print( "%f %f %f" %(roll,pitch,yaw))
        time.sleep(0.01)

