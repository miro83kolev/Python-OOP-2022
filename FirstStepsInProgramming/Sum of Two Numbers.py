start_interval=int(input())
end_interval=int(input())
magic_number=int(input())

counter = 0
combination_has_been_found=False

for x in range(start_interval, end_interval+1):
    for y in range(start_interval, end_interval+1):
        counter +=1
        if x+y==magic_number:
            print(f'Combination N:{counter} ({x} + {y} = {magic_number})')
            combination_has_been_found=True
            break
    if combination_has_been_found:
        break

if not combination_has_been_found:
    print(f'{counter} combinations - neither equals {magic_number}')