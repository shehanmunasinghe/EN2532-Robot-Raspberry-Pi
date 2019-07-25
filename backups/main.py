import time
import os

from ToFs import ToFs
from Robot_Slave import Robot_Slave


if __name__ == "__main__":
    print("This process has the PID", os.getpid())

    toFs=ToFs()
    time.sleep(0.1)
    robot_Slave=Robot_Slave()

    #for i in range(1, 101):
    while True:
        tof_right_2,tof_right_1,tof_front,tof_left_1,tof_left_2 = toFs.getMeasurements()
        print(" %f %f %f %f %f " %(tof_right_2,tof_right_1,tof_front,tof_left_1,tof_left_2))
        robot_Slave.write_ToF_measurements(tof_right_2,tof_right_1,tof_front,tof_left_1,tof_left_2)

    #print("Time: %d"%(end_time-start_time))
