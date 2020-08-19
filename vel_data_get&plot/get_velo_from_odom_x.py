#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

result = []
warn1 = "x:"
output = open('1.0_control_vel_x.txt', 'w')
marker = 1
with open('1.0_odom.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if (warn1 in line):
            velo_str = re.split("x: ", line)[1]
            if marker == 1:
                print velo_str
                output.write(velo_str)
                result.append(velo_str)
                marker = 0
            else:
                marker = 1

print result
output.close
