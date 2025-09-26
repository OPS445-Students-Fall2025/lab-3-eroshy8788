#!/usr/bin/env python3
'''Lab 3 Part 2 - free disk space'''
# Author ID: eroshy   # <-- replace with your Seneca ID if needed

import subprocess

def free_space():
    # Runs a shell command to find free space on the root filesystem
    cmd = "df -h | grep '/$' | awk '{print $4}'"
    p = subprocess.Popen(cmd,
                         stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True)
    output = p.communicate()
    stdout = output[0].decode('utf-8').strip()
    return stdout

if __name__ == '__main__':
    print(free_space())
