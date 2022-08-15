hours = int(input())
minutes = int(input())

minutes_plus_15 = minutes+15

if minutes_plus_15>59:
    minutes_plus_15 -=60
    hours +=1

if hours==24:
    hours=0

if minutes_plus_15<10:
    print(f'{hours}:0{minutes_plus_15}')
else:
    print(f'{hours}:{minutes_plus_15}')