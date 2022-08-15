actor_name = input()
point_academy = float(input())
jury = int(input())

points=0
sum=0

for i in range(jury):
    jury_name=input()
    jury_points=float(input())

    points=point_academy+(len(jury_name)*jury_points/2);
    sum +=points
    point_academy=points

    if point_academy>1250.5:
        break

points_needed=1250.5-points

if points>1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {points_needed:.1f} more!')