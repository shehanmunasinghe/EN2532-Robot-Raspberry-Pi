import time
import VL53L0X
import os

class ToFs:
    def __init__(self):
       # Create a VL53L0X objects for devices on TCA9548A buses 2,3,4,5,6
        self.tof1 = VL53L0X.VL53L0X(tca9548a_num=2, tca9548a_addr=0x70)
        self.tof2 = VL53L0X.VL53L0X(tca9548a_num=3, tca9548a_addr=0x70)
        self.tof3 = VL53L0X.VL53L0X(tca9548a_num=4, tca9548a_addr=0x70)
        self.tof4 = VL53L0X.VL53L0X(tca9548a_num=5, tca9548a_addr=0x70)
        self.tof5 = VL53L0X.VL53L0X(tca9548a_num=6, tca9548a_addr=0x70)

        self.tof1.open()
        self.tof2.open()
        self.tof3.open()
        self.tof4.open()
        self.tof5.open()

        # Start ranging on TCA9548A bus 1
        self.tof1.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
        self.tof2.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
        self.tof3.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
        self.tof4.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
        self.tof5.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)

        self.timing = self.tof1.get_timing()
        if self.timing < 20000:
            self.timing = 20000
        print("Timing %d ms" % (self.timing/1000))

        print(time.time())
   
    def getMeasurements(self):
        tof_right_2 = self.tof1.get_distance()
        tof_right_1 = self.tof2.get_distance()
        tof_front = self.tof3.get_distance()
        tof_left_1 = self.tof4.get_distance()
        tof_left_2 = self.tof5.get_distance()

        #print("%d , %d , %d, %d , %d" % (tof_right_2,tof_right_1,tof_front,tof_left_1,tof_left_2))
        #print("")
        # if (tof_right_2<0 or tof_right_1<0  or tof_front<0 or tof_left_1<0 or tof_left_2<0):
        #     print("Sensors not powered")
        #     time.sleep(2)
        #     self.reconnect()
        #     return 0,0,0,0,0
        #     #raise Exception
        # else:
        #     #time.sleep(self.timing/1000000.00)
        #     return tof_right_2,tof_right_1,tof_front,tof_left_1,tof_left_2
        return tof_right_2,tof_right_1,tof_front,tof_left_1,tof_left_2

        #time.sleep(self.timing/1000000.00)

    def stop(self):
        self.tof1.stop_ranging()
        self.tof2.stop_ranging()
        self.tof3.stop_ranging()
        self.tof4.stop_ranging()
        self.tof5.stop_ranging()

        self.tof1.close()
        self.tof2.close()
        self.tof3.close()
        self.tof4.close()
        self.tof5.close()
    
'''    def reconnect(self):
        print("Reconnecting....")
        self.stop()
       # Create a VL53L0X objects for devices on TCA9548A buses 2,3,4,5,6
        self.tof1 = VL53L0X.VL53L0X(tca9548a_num=2, tca9548a_addr=0x70)
        self.tof2 = VL53L0X.VL53L0X(tca9548a_num=3, tca9548a_addr=0x70)
        self.tof3 = VL53L0X.VL53L0X(tca9548a_num=4, tca9548a_addr=0x70)
        self.tof4 = VL53L0X.VL53L0X(tca9548a_num=5, tca9548a_addr=0x70)
        self.tof5 = VL53L0X.VL53L0X(tca9548a_num=6, tca9548a_addr=0x70)

        self.tof1.open()
        self.tof2.open()
        self.tof3.open()
        self.tof4.open()
        self.tof5.open()

        # Start ranging on TCA9548A bus 1
        self.tof1.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
        self.tof2.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
        self.tof3.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
        self.tof4.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
        self.tof5.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)'''


if __name__ == "__main__":
    print("This process has the PID", os.getpid())

    ToFs=ToFs()
    start_time=time.time()
    for i in range(1, 101):
        print(ToFs.getMeasurements())
    end_time=time.time()
    ToFs.stop

    print("Time: %d"%(end_time-start_time))
