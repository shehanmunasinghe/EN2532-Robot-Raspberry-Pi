import socket

from ToFs_Threaded import ToFs

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tofs=ToFs()
tofs.start()

while True:
    try:
        tof_right_2,tof_right_1,tof_front,tof_left_1,tof_left_2 = tofs.getMeasurements()
        print(tof_right_2,tof_right_1,tof_front,tof_left_1,tof_left_2)
        s = "%05d %05d %05d %05d %05d" %(tof_right_2,tof_right_1,tof_front,tof_left_1,tof_left_2)
        socket.sendto(s.encode("utf-8"), ("0.0.0.0",9999))
    except KeyboardInterrupt:
        tofs.stop()
        exit()