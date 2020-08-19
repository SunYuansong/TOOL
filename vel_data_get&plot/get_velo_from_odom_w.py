#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

result = []
warn1 = "z:"
output = open('2.0_control_vel_w.txt', 'w')
marker = 1
with open('2.0_odom.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if (warn1 in line):
            velo_str = re.split("z: ", line)[1]
            if marker == 0:
                print velo_str
                output.write(velo_str)
                result.append(velo_str)
                marker = 1
            else:
                marker = 0

print result
output.close
