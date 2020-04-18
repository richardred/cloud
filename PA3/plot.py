#!/usr/bin/python
import sys
#import matplotlib.pyplot as plt

temps2, temps12, temps19, times2, times12, times19 = ([] for i in range(6))
for line in sys.stdin:
    line = line.strip()
    #print(line)
    Time, TargetTemp, ActualTemp, BuildingID, sys_bID = line.split('\t')
    Time = Time.split(':')
    BuildingID = int(BuildingID)

    try:
        hours = int(Time[0])
    except ValueError:
        continue

    if hours > 8 and hours < 17:
        if BuildingID == 2:
            temps2.append(int(ActualTemp))
            times2.append(hours)
        elif BuildingID == 12:
            temps12.append(int(ActualTemp))
            times12.append(hours)
        elif BuildingID == 19:
            temps19.append(int(ActualTemp))
            times19.append(hours)          

plt.plot(times2, temps2)
plt.plot(times12, temps12)
plt.plot(times19, temps19)        

plt.ylabel('Average Temperatures of Buildings #2, 12, and 19 from 8am to 5pm')
plt.show()