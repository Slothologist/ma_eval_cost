#!/bin/bash

# This script will create a virtual microphone for PulseAudio to use and set it as the default device.
# Originally by https://stackoverflow.com/a/43553706/8155003

# Load the "module-pipe-source" module to read audio data from a FIFO special file.
echo "Creating virtual microphone."
pactl load-module module-pipe-source source_name=virtmic file=/home/rfeldhans/audioFiles/virtmic format=s16le rate=16000 channels=1

# Set the virtmic as the default source device.
echo "Set the virtual microphone as the default device."
pactl set-default-source virtmic

# Create a file that will set the default source device to virtmic for all PulseAudio client applications.
echo "default-source = virtmic" > /home/rfeldhans/.config/pulse/client.conf

# Write the audio file to the named pipe virtmic. This will block until the named pipe is read.
echo "Writing audio file to virtual microphone."
ffmpeg -re -i /home/rfeldhans/Music/all_in_one.wav -f s16le -ar 16000 -ac 1 -  > /home/rfeldhans/audioFiles/virtmic
