import math

num_tournaments = int(input())
starting_points=int(input())

current_stage=""
num_tournaments_won=0
points = 0
percents=0
average_points=0
points=starting_points

for i in range(num_tournaments):
    stage_of_tournament=input()

    if stage_of_tournament=="W":
        points +=2000
        num_tournaments_won +=1
    elif stage_of_tournament=="F":
        points +=1200
    elif stage_of_tournament=="SF":
        points +=720

average_points=(points-starting_points)/num_tournaments
percents=(num_tournaments_won/num_tournaments)*100

print(f"Final points: {points}")
print(f'Average points: {math.floor(average_points)}')
print(f'{percents:.2f}%')