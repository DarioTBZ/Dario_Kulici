#!/bin/bash

#Funktion zur Anzeige der Systeminformationen
display_system_info() {
    echo "----------------------------------------"
    echo "Timestamp: $(date '+%Y-%m-%d %H:%M:%S')"
    echo "Uptime: $(uptime | awk -F'( |,|:)+' '{print $6,$7",",$8,"hours,",$9,"minutes"}')"
    echo "Free Disk Space: $(df -h / | awk 'NR==2 {print $4}')"
    echo "Used Disk Space: $(df -h / | awk 'NR==2 {print $3}')"
    echo "Hostname: $(hostname)"
    echo "IP Address: $(ifconfig en0 | grep 'inet ' | awk '{print $2}')"
    echo "OS Name: $(uname -s)"
    echo "OS Version: $(uname -r)"
    echo "CPU Model: $(sysctl -n machdep.cpu.brand_string)"
    echo "CPU Cores: $(sysctl -n hw.ncpu)"
    echo "Total Memory: $(vm_stat | grep "Pages free" | awk '{print $3*4096/1024/1024 " MB"}')"
    echo "Used Memory: $(vm_stat | grep "Pages active" | awk '{print $3*4096/1024/1024 " MB"}')"
    echo "Free Memory: $(vm_stat | grep "Pages inactive" | awk '{print $3*4096/1024/1024 " MB"}')"
    echo "----------------------------------------"
}

#Programm
output_file=false

#Schaut ob -f angegeben wurde
if [ "$1" == "-f" ]; then
    output_file=true
fi

#Systeminformationen
if [ "$output_file" = true ]; then
    log_file="$(date '+%Y-%m')-sys-$(hostname).log"
    display_system_info >> "$log_file"
else
    display_system_info
fi

