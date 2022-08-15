inpt = input()
total_steps=0

while inpt !='Going home':
    current_steps = int(inpt)
    total_steps +=current_steps
    if total_steps>=10000:
        break
    inpt = input()

if total_steps<10000:
    going_home_steps = int(input())
    total_steps +=going_home_steps

if total_steps>=10000:
    print('Goal reached! Good job!')
    print(f'{total_steps - 10000} steps over the goal!')
else:
    print(f'{10000-total_steps} more steps to reach goal.')
