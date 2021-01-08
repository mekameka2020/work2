// SPDX-License-Identifier: GPL-3.0-only
/*
 * Copyright (C) 2021 Kawano Hidetoshi and Ryuichi Ueda.  All rights reserved.
 
 This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

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
   
    while not rospy.is_shutdown(): #ここでsub1,sub2両方読もうとしてるのが2回表示の要因
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
