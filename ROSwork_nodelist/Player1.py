#!/usr/bin/env python3

#Player 1

import rospy
from std_msgs.msg import Int32

if __name__ == '__main__':
    rospy.init_node('Player1')
    pub1 = rospy.Publisher('Player1_up', Int32, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        call = input("->")
        num1 = int(call)
        pub1.publish(num1)
        rate.sleep()
