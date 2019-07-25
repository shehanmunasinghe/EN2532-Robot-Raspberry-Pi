#!/usr/bin/python

# MIT License
# 
# Copyright (c) 2017 John Bryan Moore
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time
import VL53L0X

import os

print("This process has the PID", os.getpid())
time.sleep(1)


# Create a VL53L0X objects for devices on TCA9548A buses 2,3,4,5,6
tof1 = VL53L0X.VL53L0X(tca9548a_num=2, tca9548a_addr=0x70)
tof2 = VL53L0X.VL53L0X(tca9548a_num=3, tca9548a_addr=0x70)
tof3 = VL53L0X.VL53L0X(tca9548a_num=4, tca9548a_addr=0x70)
tof4 = VL53L0X.VL53L0X(tca9548a_num=5, tca9548a_addr=0x70)
tof5 = VL53L0X.VL53L0X(tca9548a_num=6, tca9548a_addr=0x70)

tof1.open()
tof2.open()
tof3.open()
tof4.open()
tof5.open()

# Start ranging on TCA9548A bus 1
tof1.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
tof2.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
tof3.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
tof4.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)
tof5.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)

timing = tof1.get_timing()
if timing < 20000:
    timing = 20000
print("Timing %d ms" % (timing/1000))

print(time.time())

for count in range(1, 101):
    # Get distance from VL53L0X  on TCA9548A bus 1
    distance = tof1.get_distance()
    if distance > 0:
        print("1: %d mm, %d cm, %d" % (distance, (distance/10), count))

    # Get distance from VL53L0X  on TCA9548A bus 2
    distance = tof2.get_distance()
    if distance > 0:
        print("2: %d mm, %d cm, %d" % (distance, (distance/10), count))
    
    # Get distance from VL53L0X  on TCA9548A bus 2
    distance = tof3.get_distance()
    if distance > 0:
        print("3: %d mm, %d cm, %d" % (distance, (distance/10), count))

    # Get distance from VL53L0X  on TCA9548A bus 2
    distance = tof4.get_distance()
    if distance > 0:
        print("4: %d mm, %d cm, %d" % (distance, (distance/10), count))

    # Get distance from VL53L0X  on TCA9548A bus 2
    distance = tof5.get_distance()
    if distance > 0:
        print("5: %d mm, %d cm, %d" % (distance, (distance/10), count))

    print("")

    time.sleep(timing/1000000.00)

    #time.sleep(0.2)

print(time.time())

tof1.stop_ranging()
tof2.stop_ranging()
tof3.stop_ranging()
tof4.stop_ranging()
tof5.stop_ranging()

tof1.close()
tof2.close()
tof3.close()
tof4.close()
tof5.close()
