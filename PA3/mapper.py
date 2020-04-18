#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip().split(',')
    
    if len(line) == 7:
        Time = line[1]
        TargetTemp = line[2]
        ActualTemp = line[3]
        System = line[4]
        BuildingID = line[6]
        system_buildingID = 'System ' + System + ', building ID ' + BuildingID

        print('%s\t%s\t%s\t%s\t%s' % (Time, TargetTemp, ActualTemp, BuildingID, system_buildingID))