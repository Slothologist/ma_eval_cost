import rospy
from std_msgs.msg import String
from esiaf_ros.msg import EsiafRosMsg
from threading import Lock

player_topic = '/esiaf/wav_player/finished_playing'
orc_topic = '/esiaf_ros/synchronized/speech'

logfile_name = './saved_time/p2.txt'
logfile = open(logfile_name, 'w', 1)

lock = Lock()
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


def player_sub_fn(message):
    filename = str(message)[-7:-5]
    with lock:
        okay = False
        time = ''
        for (entry, time_took) in orc_msgs:
            if filename_to_utterance[filename] in entry:
                okay = True
                time = time_took
        logfile.write('\nrecognition\n' if okay else '\nno recognition\n')
        logfile.write('time: ' + str(time) + '\n')
        if len(orc_msgs) > 1:
            logfile.write('more than one recognition\n')


def orc_sub_fn(message):
    act_time = rospy.get_rostime()
    utterance = message.speechInfo[0].hypotheses[0].recognizedSpeech
    dur = act_time - message.speechInfo[0].duration.finish
    time_took = str(dur.to_sec()) + ' secs'
    with lock:
        orc_msgs.append((utterance, time_took))


rospy.init_node('time_and_wer_saver')

orc_sub = rospy.Subscriber(orc_topic, EsiafRosMsg, orc_sub_fn)
player_sub = rospy.Subscriber(player_topic, String, player_sub_fn)


def kill_p(signal):
    orc_sub.unregister()
    player_sub.unregister()
    logfile.close()
    rospy.signal_shutdown('successfully finished')
    exit(0)

sub = rospy.Subscriber('/esiaf/wav_player/shutdown', String, kill_p)

rospy.loginfo('Ready!')

rospy.spin()

