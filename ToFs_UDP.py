import socket
import threading
import os

class ToFs_UDP(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(("0.0.0.0", 9999))

        self.tof_right_2 = 0
        self.tof_right_1 = 0
        self.tof_front   = 0
        self.tof_left_1  = 0
        self.tof_left_2  = 0

    def run(self):
        while True:
            try:
                data = self.socket.recv(80).split()
                data=[item.decode('utf-8') for item in data]
                #print(data)
                if(len(data)>=5):
                    self.tof_right_2 =int(data[0])
                    self.tof_right_1 =int(data[1])
                    self.tof_front   = int(data[2])
                    self.tof_left_1  = int(data[3])
                    self.tof_left_2  = int(data[4])
            except KeyboardInterrupt:
                exit()
    
    def getMeasurements(self):        
        if (self.tof_right_2 ==-1 or self.tof_right_1 == -1 or self.tof_front==-1 or self.tof_left_1==-1 or self.tof_left_2==-1) :
            return 0,0,0,0,0
        return self.tof_right_2,self.tof_right_1,self.tof_front,self.tof_left_1,self.tof_left_2


if __name__ == "__main__":
    print("This process has the PID", os.getpid())

    tofs_udp=ToFs_UDP()
    tofs_udp.start()

    while True:
        print(tofs_udp.getMeasurements())
    