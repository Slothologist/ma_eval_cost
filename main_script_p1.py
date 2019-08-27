import subprocess
import time
from threading import Thread


def subprocess_cmd(command):
    print(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print(proc_stdout)


prefix = '/vol/systems/speech-pipeline-melodic/'
ALSA_DEVICE = 'default'
VDEMO_PSA_CONFIG = '/home/rfeldhans/programming/audio/ma_eval_cost/pipeline1_psa_config.conf'
PSA_MODEL = prefix + '/share/pocketsphinx/model/de-de/de-de'
PSA_DICT = prefix + '/share/pocketsphinx/tobiDic_ger.dic'


t_1 = Thread(target=subprocess_cmd, args=('./install_virtmic.sh',))
t_1.start()

time.sleep(2)

t4 = Thread(target=subprocess_cmd, args=('./play_virtmic.sh',))
t4.start()

# start time and wer saver
t1 = Thread(target=subprocess_cmd, args=('python save_time_and_wer_p1.py',))
t1.start()

# start wav player

t2 = Thread(target=subprocess_cmd, args=([prefix + '/bin/pocketsphinx_adapter ' + VDEMO_PSA_CONFIG + ' --hmm=' + PSA_MODEL + ' --dict=' + PSA_DICT + ' --alsa-device=' + ALSA_DEVICE],))
t2.start()

# wait a sec
time.sleep(1)

# start cpu saver
t3 = Thread(target=subprocess_cmd, args=('python save_cpu_p1.py config_p1.yaml',))
t3.start()


t_1.join()
t1.join()
# t2.join()
t3.join()
t4.join()

t5 = Thread(target=subprocess_cmd, args=('./uninstall_virtmic.sh',))
t5.start()
t5.join()

print('finished!')

