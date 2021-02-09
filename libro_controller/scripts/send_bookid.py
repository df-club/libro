#!/usr/bin/env python
# coding:utf-8

# 发布通过（二维码）识别所得的bookid信息，作为bookid_srv服务的client端
# 在程序中可添加关于二维码识别相关代码

# 加载所需模块
import rospy
from libro_controller.srv import BookID

def send_bookid():
    rospy.init_node('send_bookid')
    # 等待有可用的服务 "bookid"
    rospy.wait_for_service("bookid_srv")
    try:
        # 定义service客户端，service名称为“bookid”，service类型为bookid
        bookid_client = rospy.ServiceProxy("bookid_srv", BookID)
        # 向server端发送请求，发送的request内容为bookid
        # 这里的bookid是通过二维码识别获取的
        bookid = 1
        resp = bookid_client.call(bookid)
        # 打印处理结果，注意调用response的方法，类似于从resp对象中调取response属性
        rospy.loginfo("Message From server:%s",resp.feedback)
    except rospy.ServiceException:
        rospy.logwarn("Service call failed: %s",rospy.ServiceException)

# 如果单独运行此文件，则将上面函数send_bookid()作为主函数运行
if __name__=="__main__":
    send_bookid()