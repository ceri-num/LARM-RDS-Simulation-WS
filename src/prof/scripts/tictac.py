#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from prof import srv

# Program parameter:
rospy.init_node('tictac', anonymous=True)
pub = rospy.Publisher('tic', String, queue_size=10)
rate = rospy.Rate(1) # 1hz
msgs= ['tic', 'tac']

# ROS callback
def rate_service( data ):
    global rate
    rate= rospy.Rate( data.Value )
    return 1

# ROS node configuration
rospy.Service('rate', srv.Rate, rate_service)

# Program loop:
i= 0
while not rospy.is_shutdown():
    # publishing
    pub.publish(msgs[i])
    rospy.loginfo(msgs[i])
    # increment
    i= (i+1)%len(msgs)
    # Wait
    rate.sleep()

# # Timer version :
# rate = rospy.Duration(1) 
# def my_callback(event):
#    hello_str = "tic %s" % rospy.get_time()
#    pub.publish(hello_str)
# rospy.Timer(rate, my_callback)
# rospy.spin()
