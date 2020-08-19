#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

result = []
warn1 = "alarm off OK"
warn2 = "alarm on OK"
output = open('2.0_control_vel.txt', 'w')
with open('2.0_imu_info.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if (line[0] != 'd') or (warn1 in line) or (warn2 in line):
            continue
        velo_str = re.split("velo|dist", line)[1]
        print velo_str
        output.write(velo_str)
        output.write('\n')
        result.append(velo_str)
print result
output.close
