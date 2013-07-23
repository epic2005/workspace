#!/usr/bin/env python

import sys
import datetime

MONTH = {
    'Jan':1,
    'Feb':2,
    'Mar':3,
    

}


def tailFile(f,lines):
    from subprocess import Popen, PIPE
    cmd = "tail -n %s %s"
    p = Popen(cmd, stdout=PIPE, shell=True)
    stdout, stderr = p.communicate()
    return stdout

def convert2datetime(s):
    now = datetime.datetime.now()
    month, day, time =  s.split()
    hour, minute, second =  time.split(':')
    t = datetime.datetime(now.year,)
    
