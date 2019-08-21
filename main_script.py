import subprocess
import time


def subprocess_cmd(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print(proc_stdout)


source = 'source /home/rfeldhans/programming/audio/workspace/install/setup.bash; '

# start time and wer saver
subprocess_cmd(source + 'python save_time_and_wer.py')

# start wav player
subprocess_cmd(source + 'roslaunch esiaf_wav_player wav_player.launch path_to_config:=/home/rfeldhans/programming/audio/workspace/install/share/esiaf_wav_player/config/eval_pipeline_2.yaml')

# wait a sec
time.sleep(1)

# start cpu saver
subprocess_cmd(source + 'python save_cpu.py config.yaml')

while True:
    time.sleep(10)
