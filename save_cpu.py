import psutil
import sys
import yaml
import rospy
from std_msgs.msg import String


def any_process_in(processes, y):
    list_of_process_names_in_y = [i for i in processes if i in y]
    return len(list_of_process_names_in_y) > 0


def aquire_processes(config):
    process_names = config['processes']
    ignore = config['ignore']
    all_processes = [psutil.Process(id) for id in psutil.pids()]
    target_processes = [x for x in all_processes if [y for y in x.cmdline() if any_process_in(process_names, y)] and x.name() not in ignore]

    # filter out children
    processes = [x for x in target_processes if x.ppid() not in [y.pid for y in target_processes]]

    print('Processes aquired:')
    for process in processes:
        print(process.cmdline()[2])

    processes = [[x.cpu_times(), x] for x in processes]  # some reordering

    return processes


# read config
print('Loading config...')
argv = sys.argv
if len(argv) < 2:
    print('Need path to configfile as first parameter!')
    exit('1')
path_to_config = argv[1]
config = yaml.safe_load(open(path_to_config))
processes = aquire_processes(config)

for process in processes:
    process[1].cpu_percent()  # call once, to initialize

files = [open(config['save_dir'] + 'esiaf_wav_player' + '.txt', 'w') if 'esiaf_wav_player' in x.cmdline()[2] else open(config['save_dir'] + x.cmdline()[2] + '.txt', 'w') for _, x in processes]  # open all required files


def kill_p(bla):
    for process_no in range(len(processes)):
        old_cpu_times, process = processes[process_no]
        act_cpu_time = sum(process.cpu_times()) - sum(old_cpu_times)
        files[process_no].write('Runtime on CPU\n')
        files[process_no].write(str(act_cpu_time))
        files[process_no].write('\nPercentage\n')
        files[process_no].write(str(process.cpu_percent()) + '\n\n')

    for f in files:
        f.close()
    rospy.signal_shutdown('finished')

rospy.init_node('save_cpu_node')
sub = rospy.Subscriber('/esiaf/wav_player/shutdown', String, kill_p)

print('Ready!')

rospy.spin()
