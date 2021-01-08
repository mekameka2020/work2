// SPDX-License-Identifier: GPL-3.0-only
/*
 * Copyright (C) 2020 Kawano Hidetoshi and Ryuichi Ueda.  All rights reserved.
 
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
