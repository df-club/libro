#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 根据bookid信息设定并发布libro的导航目标位姿信息
import rospy
# Brings in the SimpleActionClient
import actionlib
from libro_controller.srv import BookID, BookIDResponse
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# 作为bookid_srv的服务的server端获取所发送的bookid
def setgoal_by_bookid():
    rospy.init_node("setgoal_by_bookid")
    # 定义service的server端，service名称为"bookid"， service类型为bookid
    # 收到的request请求信息将作为参数传递给handle_function进行处理
    rospy.Service("bookid_srv", BookID, handle_function)
    rospy.loginfo("Ready to handle the bookid request:")
    # 阻塞程序结束
    rospy.spin()

# Define the handle function to handle the request inputs
def handle_function(req):
    # 注意我们是如何调用request请求内容的，与前面client端相似，都是将其认为是一个对象的属性，通过对象调用属性，在我们定义
    rospy.loginfo('Request bookid %d'%req.bookid)
    if req.bookid <= 0:
        rospy.loginfo('Invalid bookid')
    else:
        # 调用导航action
        setgoal_client(req.bookid)
    # 返回一个Service_demoResponse实例化对象，其实就是返回一个response的对象，其包含的内容为我们再Service_demo.srv中定义的
    # response部分的内容，我们定义了一个string类型的变量，因此，此处实例化时传入字符串即可
    return BookIDResponse("Recived bookid %d"%req.bookid)

# 根据bookid设定导航目标
def setgoal_client(bookid):
    rospy.loginfo("Bookid for navigation: %d"%bookid)
    # Initializes a rospy node to let the SimpleActionClient publish and subscribe
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()
    # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    # 构造位姿信息（可通过数据库通过bookid获取）:
    # position（位置）：x,y,z
    # orientation（方向）：x,y,z,w（四元数）
    # Move 0.5 meters forward along the x axis of the "map" coordinate frame
    goal.target_pose.pose.position.x = 0.5
    goal.target_pose.pose.position.y = 0.5
    goal.target_pose.pose.position.z = 0.0
    # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 0.0
    goal.target_pose.pose.orientation.w = 1.0
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

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    setgoal_by_bookid()
