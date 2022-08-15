import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_for_1m = float(input())

needed_time = distance_in_meters*time_for_1m
resistance_time = math.floor(distance_in_meters/15)*12.5
total_time=needed_time+resistance_time
time_difference = abs(total_time-record_in_seconds)

if total_time<record_in_seconds:
   print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {time_difference:.2f} seconds slower.")
