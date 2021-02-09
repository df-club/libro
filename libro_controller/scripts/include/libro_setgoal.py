#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 用于设定并发布libro的导航目标位姿信息
import rospy
# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import sys

def movebase_client(inputX,inputY):
   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()
   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    # 构造位姿信息（可通过数据库获取）:
    # position（位置）：x,y,z
    # orientation（方向）：x,y,z,w（四元数）
   # Move 0.5 meters forward along the x axis of the "map" coordinate frame
    goal.target_pose.pose.position.x = inputX
    goal.target_pose.pose.position.y = inputY
    goal.target_pose.pose.position.z = 0.0
   # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 0.0
    goal.target_pose.pose.orientation.w = 1.0
    rospy.loginfo("Navigation goal:")
    rospy.loginfo(goal.target_pose.pose)
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
        return client.get_result()