#!/usr/bin/env python3

# Show Sum & Winner


import rospy
from std_msgs.msg import Int32



n = 0 
m = 0 

sumn = 0
num1 = 0
num2 = 0 
time = 0

def cb(message):
    global n
    n = message.data
    global m 
    m = message.data 



pub1 = rospy.Publisher('Player1_up', Int32, queue_size=1)
pub2 = rospy.Publisher('Player2_up', Int32, queue_size=1) 


if __name__ == '__main__':
    rospy.init_node('judgement')
    rate = rospy.Rate(1)
   
    while not rospy.is_shutdown(): 
        sub1 = rospy.Subscriber('Player1_up', Int32, cb)
        
        if n <= 0 | n >= 10 :
            print("この数字は使えません。")
            num1 = 0
            pub1.publish(num1)
        elif n == 0:
            num1 = 0
        else:
            num1 = int(n)
            if num2 != 0:
                sumn += num1
                print(sumn)
            num1 = 0
            pub1.publish(num1)

        if sumn >= 100:
            print("Winner Player2!!")
            exit()

        sub2 = rospy.Subscriber('Player2_up', Int32, cb)
        
        if m <= 0 | m >= 10:
            print("この数字は使えません。")
            num2 = 0
            pub2.publish(num2)
        elif m == 0:
            num2 = 0
        else:
            num2 = int(m)
            sumn += num2 
            print(sumn)
            num2 = 0
            pub2.publish(num2)
        if sumn >= 100:
            print("Winner Player1!!")
            exit()
        rate.sleep()
