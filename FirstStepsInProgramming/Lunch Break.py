import math

movie_series = str(input())
episode_duration = float(input())
lunchbreak_duration = float(input())

time_for_lunch = lunchbreak_duration*0.125
time_for_relax = lunchbreak_duration*0.25
time_left = lunchbreak_duration-(time_for_lunch+time_for_relax)
difference = abs(episode_duration-time_left)

if time_left>=episode_duration:
    print(f"You have enough time to watch {movie_series} and left with {math.ceil(difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_series}, you need {math.ceil(difference)} more minutes.")