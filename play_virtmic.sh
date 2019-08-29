#!/usr/bin/env bash

echo "sourcing ros..."
source /home/rfeldhans/programming/audio/workspace/install/setup.bash

echo "starting..."
python publish_rostime_now.py

# Write the audio file to the named pipe virtmic. This will block until the named pipe is read.
#echo "Writing audio file to virtual microphone."
while true; do
    ffmpeg -re -i /home/rfeldhans/Music/all_in_one.wav -f s16le -ar 16000 -ac 1 -  > /home/rfeldhans/audioFiles/virtmic
    rostopic pub /esiaf/wav_player/shutdown std_msgs/String "data: ''" -1
done