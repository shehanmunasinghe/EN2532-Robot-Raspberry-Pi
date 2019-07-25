# Copyright Pololu Corporation.  For more information, see https://www.pololu.com/
import smbus
import struct
import time

class Robot_Slave:
  def __init__(self):
    self.bus = smbus.SMBus(1)

  def reconnect(self):
    self.bus = smbus.SMBus(1)
  #Helper Functions
  def read_unpack(self, address, size, format):
    # Ideally we could do this:
    #    byte_list = self.bus.read_i2c_block_data(20, address, size)
    # But the AVR's TWI module can't handle a quick write->read transition,
    # since the STOP interrupt will occasionally happen after the START
    # condition, and the TWI module is disabled until the interrupt can
    # be processed.
    #
    # A delay of 0.0001 (100 us) after each write is enough to account
    # for the worst-case situation in our example code.

    self.bus.write_byte(20, address)
    time.sleep(0.0001)
    byte_list = [self.bus.read_byte(20) for _ in range(size)]    
    #print(byte_list)
    #print(struct.unpack(format, bytes(byte_list)))
    return struct.unpack(format, bytes(byte_list))
    
  def write_pack(self, address, format, *data):
    data_array = list(struct.pack(format, *data))
    #print(data_array)
    try:
      self.bus.write_i2c_block_data(20, address, data_array)
      time.sleep(0.0001)
    except OSError :
      print("Arduino disconnected. Reconnecting ....")
      time.sleep(0.5)
      self.reconnect()


  #Write to buffer
  def write_ToF_measurements(self, tof_right_2,tof_right_1,tof_front,tof_left_1,tof_left_2):
    self.write_pack(2, 'HHHHH',tof_right_2,tof_right_1,tof_front,tof_left_1,tof_left_2)

  def write_IMU_status(self,pitch, tof_front):
    if( (tof_front<300 and tof_front>50 and pitch<5) or (pitch<-15) ):
      print("Ramp Ahead or Climb")
      self.write_pack(12,'B',1)
    elif(pitch>14):
      print("Ramp Descent")
      self.write_pack(12,'B',2)
    else:
      print("Flat Surface")
      self.write_pack(12, 'B', 0)


  #Read from Buffer

  def read_analog(self):
    return self.read_unpack(0, 2, "H")
    
"""   def read_check_IMU_status_flag(self):
    return self.read_unpack(7, 1,"B") """

"""   def read_buttons(self):
    return self.read_unpack(3, 3, "???")

  def read_battery_millivolts(self):
    return self.read_unpack(10, 2, "H") """


"""   def play_notes(self, notes):
    self.write_pack(24, 'B15s', 1, notes.encode("ascii"))

  def motors(self, left, right):
    self.write_pack(6, 'hh', left, right) """

"""   def read_encoders(self):
    return self.read_unpack(39, 4, 'hh')

  def test_read8(self):
    self.read_unpack(0, 8, 'cccccccc')

  def test_write8(self):
    self.bus.write_i2c_block_data(20, 0, [0,0,0,0,0,0,0,0])
    time.sleep(0.0001) """

if __name__ == "__main__":
    robot_Slave=Robot_Slave()
    while True:
      #s=format(robot_Slave.read_analog()[0], '016b')
      #print(s)

      #robot_Slave.write_ToF_measurements(732, 410, 600, 432, 567)
      robot_Slave.write_IMU_status(-20,130)
      time.sleep(0.1)
