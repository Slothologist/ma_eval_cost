import os
import soundfile as sf
import numpy

path = '/home/rfeldhans/Music/recordings3/'

target = 'all_in_one.wav'

files = [path + x for x in os.listdir(path) if x is not target]

frames_per_second = 16000

timeout_in_seconds = 2. * 400./1000.

filler_array = numpy.zeros((int(frames_per_second * timeout_in_seconds),), numpy.int16)

with sf.SoundFile(path + target, 'w', samplerate=16000, channels=1) as target_file:
    for file in files:
        [target_file.write(block) for block in sf.blocks(file, blocksize=512)]
        target_file.write(filler_array)

exit(0)