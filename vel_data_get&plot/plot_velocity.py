#!/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
data1 = np.loadtxt('2.0cv.txt', delimiter=',', skiprows=1)
data2 = np.loadtxt('2.0pv.txt', delimiter=',', skiprows=1)
data3 = np.loadtxt('2.0cw.txt', delimiter=',', skiprows=1)
data4 = np.loadtxt('2.0pw.txt', delimiter=',', skiprows=1)

plt.figure(21)
plt.subplot(211)
plt.grid(True)  # 增加格点
plt.xlabel('time(s)')
plt.ylabel('velocity(m/s)')
plt.title('vel_max = 2.0')
start_time = data1[0, 0]
plt.plot((data1[:, 0]-start_time)*0.000000001,
         data1[:, 1], 'b', lw=1.6, label='control_vel')
plt.plot((data2[:, 0]-start_time)*0.000000001,
         data2[:, 1], 'r', lw=1.6, label='plan_vel')
plt.legend()

plt.subplot(212)
plt.grid(True)  # 增加格点
plt.xlabel('time(s)')
plt.ylabel('velocity(radian/s)')
plt.title('vel_max = 2.0')
start_time = data3[0, 0]
plt.plot((data3[:, 0]-start_time)*0.000000001,
         data3[:, 1], 'b', lw=1.6, label='control_vel')
plt.plot((data4[:, 0]-start_time)*0.000000001,
         data4[:, 1], 'r', lw=1.6, label='plan_vel')
plt.legend()


plt.show()
