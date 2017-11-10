# !/bin/bash
# This simple script is used for the presentation of the program

PID=$(pgrep "python")
kill -STOP $PID
echo $PID
