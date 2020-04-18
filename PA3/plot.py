#!/usr/bin/python
import sys
from collections import defaultdict
from statistics import mean
import matplotlib.pyplot as plt

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

# temp = defaultdict(set)
# for c, i in zip(times19, temps19):
#     temp[c].add(i)
# print(temp)

# line19 = dict(temp)
# print(line19)

# for st,vals in line19.items():
#     print("Average for {} is {}".format(st,mean(vals)))

plt.plot([9, 10, 11, 12, 13, 14, 15, 16], [67.53846153846153, 67, 68.38461538461539, 68.66666666666667, 72.5, 71.55555555555556, 65.38461538461539, 67.92857142857143], label='Building 2')
plt.plot([9, 10, 11, 12, 13, 14, 15, 16], [68.61538461538461, 66.36363636363636, 71.08333333333333, 71.4, 69.133, 67.57142857, 68.92857142857143, 68.83333333333333], label='Building 12')
plt.plot([9, 10, 11, 12, 13, 14, 15, 16], [69.35714285714286, 67.2, 68.5625, 68.71428571428571, 69.0625, 69.92857142857143, 69.84615384615384, 69.57142857142857], label='Building 19')
plt.legend(loc='upper left')
plt.xlabel('Time of Day (8am-5pm)')
plt.ylabel('Average Temperatures of Buildings 2, 12, and 19')
plt.show()