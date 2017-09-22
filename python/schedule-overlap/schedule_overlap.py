#!/usr/local/bin/python3
# Script to check if there are overlaps in sets, for example meeting start time.
# Mayel Espino.
#

#schedules = [(10,11),(9,9.5),(7,8),(6,7.5)]
#schedules = [(9,10.5),(10,11),(9,9.5),(7,8),(6,7.5)]
schedules = [(9,10.5),(10,11),(9,9.5),(7,8),(6,7.5)]

schedules_dic = {}
overlap = False

for schedule in schedules:
    start, end = schedule
    if start in schedules_dic.keys():
        overlap = True
        print("Overlap! there is more than one meeting that start at: {}".format(start))
        exit(0)
    else:
        schedules_dic[start] = end

start_times = list(schedules_dic.keys())
start_times.sort()

print("Start times:{}", start_times)

for index in range(len(start_times)-1):
    current_start_time = start_times[index]
    current_end_time = schedules_dic[current_start_time]
    next_start_time = start_times[index+1]
    next_end_time = schedules_dic[next_start_time]
    print("{},{}-{}".format(current_start_time, next_start_time, next_end_time))
    if current_start_time >= next_start_time and current_start_time <= next_end_time:
        overlap = True
        print("Overlap! 2: {}-{} overlaps with {}-{}".format(current_start_time, current_end_time,next_start_time, next_end_time))
        exit(0)
    elif current_end_time >= next_start_time and current_start_time <= next_end_time:
        overlap = True
        print("Overlap! 3: {}-{} overlaps with {}-{}".format(current_start_time, current_end_time,next_start_time, next_end_time))
        exit(0)

