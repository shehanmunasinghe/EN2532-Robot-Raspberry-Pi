import time
import os

from ToFs_UDP import ToFs_UDP
from Robot_Slave import Robot_Slave
from IMU import IMU


if __name__ == "__main__":
    print("This process has the PID", os.getpid())

    imu=IMU()
    imu.start()
    
    tofs_udp=ToFs_UDP()
    tofs_udp.start()
    
    time.sleep(0.1)
    robot_Slave=Robot_Slave()

    while True:
        #try:

        tof_right_2,tof_right_1,tof_front,tof_left_1,tof_left_2 = tofs_udp.getMeasurements()
        print(" ToF Readings : %d %d %d %d %d " %(tof_right_2,tof_right_1,tof_front,tof_left_1,tof_left_2))
        
        roll,pitch,yaw = imu.getEuler()
        print(" IMU Readings : %f %f %f " %(roll,pitch,yaw))	

        #check_IMU_status_flag=robot_Slave.read_check_IMU_status_flag()
        
        robot_Slave.write_ToF_measurements(tof_right_2,tof_right_1,tof_front,tof_left_1,tof_left_2)
        robot_Slave.write_IMU_status(pitch, tof_front)


