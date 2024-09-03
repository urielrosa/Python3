#!/usr/bin/env python3

import sys
import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")


if __name__ == "__main__":
	entertime = int(sys.argv[1])
	countdown(entertime)
