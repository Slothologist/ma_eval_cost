import rospy
from std_msgs.msg import Time
import time


rospy.init_node('ros_now_publisher')

sub2 = rospy.Publisher('/ps_start', Time, queue_size=1)

time.sleep(5)

sub2.publish(rospy.get_rostime())



