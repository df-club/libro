#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 用于设定并发布libro的导航目标位姿信息
import rospy
# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import sys
from include.libro_setgoal import movebase_client

def setGoal(inX,inY):
    try:
        rospy.init_node('libro_setgoal')
        result = movebase_client(inX,inY)
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")

if __name__ == '__main__':
    