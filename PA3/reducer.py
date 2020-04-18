#!/usr/bin/python
import sys

building_temps = {}
high_temps = {}
for line in sys.stdin:
    line = line.strip()
    print(line)
    Time, TargetTemp, ActualTemp, BuildingID, sys_bID = line.split('\t')
    Time = Time.split(':')
    
    temp_difference = abs(int(TargetTemp) - int(ActualTemp))
    if sys_bID in building_temps:
        building_temps[sys_bID].append(int(temp_difference))
    else:
        building_temps[sys_bID] = []
        building_temps[sys_bID].append(int(temp_difference))

    try:
        hours = int(Time[0])
    except ValueError:
        continue

    if hours > 8 and hours < 17:
        if BuildingID in high_temps:
            high_temps[BuildingID].append(int(ActualTemp))
        else:
            high_temps[BuildingID] = []
            high_temps[BuildingID].append(int(ActualTemp))
    else:
        continue

results = {}
for sys_bID in building_temps.keys():
    avg_temp_diffs = sum(building_temps[sys_bID]) * 1.0 / len(building_temps[sys_bID])

    if sys_bID in results:
        results[sys_bID].append(avg_temp_diffs)
    else:
        results[sys_bID] = []
        results[sys_bID].append(avg_temp_diffs)

sorted_results = sorted(results.items(), key=lambda x: x[1])
for x in list(reversed(list(sorted_results)))[0:3]:
    print(x)

# averages
building_temps = {}
for BuildingID in high_temps.keys():
    avg_high_temps = sum(high_temps[BuildingID]) * 1.0 / len(high_temps[BuildingID])
    if BuildingID in building_temps:
        building_temps[BuildingID].append(avg_high_temps)
    else:
        building_temps[BuildingID] = []
        building_temps[BuildingID].append(avg_high_temps)

sorted_building_temps = sorted(building_temps.items(), key=lambda x: x[1])
for x in list(reversed(list(sorted_building_temps)))[0:3]:
    print(x)