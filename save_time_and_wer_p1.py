import rospy
from std_msgs.msg import String, Time
import time

orc_topic = '/speechrec/psa/speechRecognition/simple'

logfile_name = './saved_time/p2.txt'
logfile = open(logfile_name, 'w', 1)

logfile2_name = './saved_time/p2_segmentations.txt'
logfile2 = open(logfile2_name, 'w', 1)

orc_msgs = []

filename_to_utterance = {
    '01': 'hallo flobi',
    '02': 'mein name ist',
    '03': 'ja das stimmt',
    '04': 'nein das moechte ich nicht',
    '05': 'okay ist in ordnung',
    '06': 'gut das mache ich',
    '07': 'wo kommt denn der koch loeffel hin',
    '08': 'was muss ich machen',
    '09': 'ich brauche deine hilfe',
    '10': 'mach das licht in der kueche an',
    '11': 'beleuchtung bitte',
    '12': 'wo geht das licht an',
    '13': 'schick mir flobi in die kueche',
    '14': 'kann ich was zu trinken haben',
    '15': 'ist der geschirrspueler fertig',
    '16': 'flobi wo sind die glaeser',
    '17': 'wo sind die glaeser',
    '18': 'entspannungsmodus starten',
    '19': 'ich bin fertig damit',
    '20': 'okay',
    '21': 'ja',
    '22': 'nein',
    '23': 'auf wiedersehen',
    '24': 'tschuess'
}

utterance_to_filename = {filename_to_utterance[x]: x for x in filename_to_utterance}


def orc_sub_fn(message):
    filename = message.data.strip()
    time = rospy.get_rostime()
    logfile.write('\nrecognition of ' + filename + '\n' if filename else '\nno recognition\n')
    logfile.write('time: ' + str(time) + '\n')


rospy.init_node('time_and_wer_saver')

def start_msg(msg):
    rostime = msg.data
    logfile.write('starting_time: ' + str(rostime) + '\n\n\n')

def segmentation_msg(msg):
    rostime = msg.data
    logfile2.write('segmentation time:' + str(rostime) + '\n')

orc_sub = rospy.Subscriber(orc_topic, String, orc_sub_fn)


def kill_p(signal):
    time.sleep(5)
    orc_sub.unregister()
    logfile.close()
    logfile2.close()
    rospy.signal_shutdown('successfully finished')
    exit(0)

sub = rospy.Subscriber('/esiaf/wav_player/shutdown', String, kill_p)
sub2 = rospy.Subscriber('/ps_start', Time, start_msg)
sub3 = rospy.Subscriber('/ps_adapter/segEnd/pub', Time, segmentation_msg)

rospy.loginfo('Ready!')

rospy.spin()

