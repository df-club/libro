#!/usr/bin/env python
# coding:utf-8

# 通过接收bookId，bookName等参数查找数据库获取书籍的位置信息
# 使用位置信息，调用setGoalByPos导航机器人到指定位置
# 用法：
#   通过bookId导航：findBook.py -i 100
#   通过bookName导航：findBook.py -n 西游记

import rospy
from sys import argv
import tf
import sqlite3
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from connectBookID import getPosByBookIDFromDB, getPosByBookNameFromDB 
import actionlib

# pos with the info of x, y, z, theta
def setGoalByPos(pos):
    # Initializes a rospy node to let the SimpleActionClient publish and subscribe
    rospy.init_node("setgoal_by_findBook")
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()
    # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    # 构造位姿信息（可通过数据库通过bookid获取）:
    # position（位置）：x,y,z; orientation（方向）：x,y,z,w（四元数）
    goal.target_pose.pose.position.x = pos[0]
    goal.target_pose.pose.position.y = pos[1]
    goal.target_pose.pose.position.z = pos[2]
    # No rotation of the mobile base frame w.r.t. map frame
    quat = tf.transformations.quaternion_from_euler(0,0,pos[3])
    goal.target_pose.pose.orientation.x = quat[0]
    goal.target_pose.pose.orientation.y = quat[1]
    goal.target_pose.pose.orientation.z = quat[2]
    goal.target_pose.pose.orientation.w = quat[3]
    rospy.loginfo("Navigation goal:")
    rospy.loginfo(goal.target_pose.pose)
    try:
        # Sends the goal to the action server.
        client.send_goal(goal)
         # Waits for the server to finish performing the action.
        wait = client.wait_for_result()
         # If the result doesn't arrive, assume the Server is not available
        if not wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            # Result of executing the action
            if client.get_result():
                rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")


def findBookByID(bookid):
    print("Navigation by bookId: %s"%bookid)
    pos = getPosByBookIDFromDB(bookid)
    setGoalByPos(pos)


def findBookByName(bookname):
    print("Navigation by bookName: %s"%bookname)
    pos = getPosByBookNameFromDB(bookname)
    setGoalByPos(pos)

if __name__=="__main__":
    if argv[1] == '-i':
        findBookByID(argv[2])
    elif argv[1] == '-n':
        findBookByName(argv[2])
    else:
        print("Invalid input to find Book!")
