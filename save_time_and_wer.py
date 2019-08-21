import rospy
from std_msgs.msg import String
from esiaf_ros.msg import EsiafRosMsg

player_topic = '/esiaf/wav_player/finished_playing'
orc_topic = '/esiaf_ros/synchronized/speech'


def player_sub_fn(message):
    pass


def orc_sub_fn(message):
    pass


orc_sub = rospy.Subscriber(orc_topic, EsiafRosMsg, orc_sub_fn)
player_sub = rospy.Subscriber(player_topic, String, player_sub_fn)

# start wav player

# start 


rospy.spin()

