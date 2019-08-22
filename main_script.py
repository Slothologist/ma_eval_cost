import subprocess
import time
from threading import Thread


def subprocess_cmd(command):
    print(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print(proc_stdout)



# start time and wer saver
t1 = Thread(target=subprocess_cmd, args=('python save_time_and_wer.py',))
t1.start()

# start wav player

t2 = Thread(target=subprocess_cmd, args=(['roslaunch esiaf_wav_player wav_player.launch path_to_config:=/home/rfeldhans/programming/audio/workspace/install/share/esiaf_wav_player/config/eval_pipeline_2.yaml'],))
t2.start()

# wait a sec
time.sleep(1)

# start cpu saver
t3 = Thread(target=subprocess_cmd, args=('python save_cpu.py config.yaml',))
t3.start()

t1.join()
t2.join()
t3.join()
print('finished!')
