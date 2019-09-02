import os
import soundfile as sf
import numpy
import pickle

path = '/home/rfeldhans/Music/recordings3/'


annotation_file_name = './annotated_wav_files.txt'


files = [path + x for x in os.listdir(path)]

frames_per_second = 16000
timeout_in_seconds = 2. * 1500./1000.
five_twelve_blocks = int(numpy.ceil(frames_per_second * timeout_in_seconds/512))
filler_array = numpy.zeros((five_twelve_blocks*512,), numpy.int16)
actual_timeout_frames = len(filler_array)

num_frames = 0

annots = []

with open(annotation_file_name, 'w', 1) as annotation_file:
    for file in files:
        # adding frame amount to total number of frames
        num_frames += sf.info(file).frames

        # calculating point of time in wav file in seconds
        total_time_eclipsed = num_frames / float(frames_per_second)

        # adding timeout frames to total number of frames
        num_frames += actual_timeout_frames

        file_name = file[-6:-4]

        annots.append((file_name, total_time_eclipsed))

        annotation_file.write('seconds: ' + str(total_time_eclipsed) + '\n')
        annotation_file.write('filename: ' + file_name + '\n')
        annotation_file.write('\n\n')

with open('./annotated_wav_file.pickle', 'w') as fileo:
    pickle.dump(annots, fileo)

exit(0)