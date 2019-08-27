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

