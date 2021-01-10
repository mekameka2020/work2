#!/usr/bin/env python3

#Player 2

import rospy
from std_msgs.msg import Int32


if __name__ == '__main__':
    rospy.init_node('Player2')
    pub2 = rospy.Publisher('Player2_up', Int32, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        call = input("->") 
        num2 = int(call)
        pub2.publish(num2)
        rate.sleep()
