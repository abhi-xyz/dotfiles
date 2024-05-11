#!/bin/bash

# This script uses ddcutil to get the current brightness level of a display

# Check if ddcutil is installed
# if ! command -v ddcutil &> /dev/null; then
#     echo "Error: ddcutil is not installed. Please install it using your package manager."
#    exit 1
#fi
case $1 in 
  "i")
    ddcutil setvcp 10 + 5
    ;;
  "d")
    ddcutil setvcp 10 - 5
    ;;
esac



# Get the current brightness level
brightness=$(ddcutil getvcp 10 2>&1 | grep -oP '(?<=current value = )\s*\d+' | tr -d ' ')

# Check if the brightness level was retrieved successfully
# if [ -z "$brightness" ]; then
#    echo "script failed"
#   # echo "Debugging information:"
#   # ddcutil getvcp 10
#     exit 1
# fi
notify-send -h int:value:$brightness -t 2000 "Brightness: $brightness%"
echo "$brightness"
