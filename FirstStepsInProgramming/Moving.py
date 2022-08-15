weidth = int(input())
height = int(input())
lenght = int(input())
total_room_space=weidth*height*lenght

total_space=0
difference=0

free_space=(input())

while free_space !='Done':

    boxes_space=int(free_space)
    total_space +=boxes_space

    difference = abs(total_space-total_room_space)
    if total_space>total_room_space:
        print(f'No more free space! You need {difference} Cubic meters more.')
        break
    free_space = (input())

if free_space=='Done':
    print(f'{difference} Cubic meters left.')

