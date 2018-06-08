#!/usr/bin/python

# import os




import rospy

from dynamixel_servomotor_controller import *
from xl_config import *


#from time import sleep


PROTOCOL_VERSION = 2.0


DXL_ID = 2
BAUDRATE = 57600
DEVICENAME = '/dev/ttyUSB0'

def main():
    print "start node."
    rospy.init_node("servomotor_controller")

    timer = rospy.Rate(0.5)




    motor_controller = DynamixelServomotorController(device_name = DEVICENAME, protocol_version = PROTOCOL_VERSION,\
                    baudrate = BAUDRATE, motor_config = XLConfig())
    motor_controller.current_id = DXL_ID


    motor_controller.set_operating_mode(XLConfig.OPERATING_MODE_POSITION_CONTROL_MODE)
    # motor_controller.set_operating_mode(XLConfig.OPERATING_MODE_VELOCITY_CONTROL_MODE)

    print "torque_enable: "
    motor_controller.set_torque_enable(1)

    print "id: " + str(motor_controller.id())
    print "baudrate: " + str(motor_controller.baudrate())
    print "torque_enable: " + str(motor_controller.torque_enable())
    


    speed = 0.0
    dir = 0.2
    max_speed = 0.5



    sw = False

    while not rospy.is_shutdown():
        sw ^= True

        motor_controller.set_led(int(sw))

        # motor_controller.set_goal_position(0 if sw else 180)
        motor_controller.set_goal_position(0.0)


        print "present_position: " + str(motor_controller.present_position())





        print "loop"
        
        # motor_controller.set_goal_velocity(speed)
        # print "max_position: " +  str(motor_controller.max_position_limit())
        # print "min_position: " +  str(motor_controller.min_position_limit())

        speed += dir
        if speed > max_speed:
            speed = max_speed
            dir *= -1

        if speed < -max_speed:
            speed = -max_speed
            dir *= -1

        print str(speed)

        timer.sleep()

    motor_controller.set_led(0)
    motor_controller.set_goal_velocity(0.0)
    motor_controller.end()

    
if __name__ == "__main__":
    main()