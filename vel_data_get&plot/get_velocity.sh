#!/bin/bash
rostopic echo -b 2.0.bag -p /cmd_vel/linear/x > 2.0pv.txt
rostopic echo -b 2.0.bag -p /cmd_vel/angular/z > 2.0pw.txt
rostopic echo -b 2.0.bag -p /odom/twist/twist/linear/x > 2.0cv.txt
rostopic echo -b 2.0.bag -p /odom/twist/twist/angular/z > 2.0cw.txt
rostopic echo -b 1.5.bag -p /cmd_vel/linear/x > 1.5pv.txt
rostopic echo -b 1.5.bag -p /cmd_vel/angular/z > 1.5pw.txt
rostopic echo -b 1.5.bag -p /odom/twist/twist/linear/x > 1.5cv.txt
rostopic echo -b 1.5.bag -p /odom/twist/twist/angular/z > 1.5cw.txt
rostopic echo -b 1.0.bag -p /cmd_vel/linear/x > 1.0pv.txt
rostopic echo -b 1.0.bag -p /cmd_vel/angular/z > 1.0pw.txt
rostopic echo -b 1.0.bag -p /odom/twist/twist/linear/x > 1.0cv.txt
rostopic echo -b 1.0.bag -p /odom/twist/twist/angular/z > 1.0cw.txt

