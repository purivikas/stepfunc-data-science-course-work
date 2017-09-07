

# Excerice
# implement a profiler that would show the rate of growth
# in compution of sorting a list of N integer .
# the profiler should ouput the following table:
# list_size  , sort_time , suffle_time , total_time
# 1000 , 0.00000001
# 10,000 , 0.00020
# 100,000,000 , 0

import random
import math

def do_loop(list_size_in):

    l1= range(0,list_size_in)
    t1 = datetime.datetime.now()
    random.shuffle(l1)
    l1.sort()
    t2 = datetime.datetime.now()
    diff_ = t2 - t1
    return diff_

def profile_sorting(iteration_number):

    exection_times = []

    for i in range (0,iteration_number):
        timelapse = do_loop(10 * math.pow(10,i))
        exection_times.append(timelapse)
        print (timelapse)
        return exection_times

