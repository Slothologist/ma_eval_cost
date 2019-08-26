#!/bin/bash

# Uninstall the virtual microphone.
# Originally by https://stackoverflow.com/a/43553706/8155003

pactl unload-module module-pipe-source
rm /home/rfeldhans/.config/pulse/client.conf
