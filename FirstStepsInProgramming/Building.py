floors_count=int(input())
rooms_count=int(input())

for floor in range(floors_count,0,-1):
    for room in range(0, rooms_count):
        if floor==floors_count:
            print("L{0}{1} ".format(floor,room), end="")
        elif floor %2==0:
            print("O{0}{1} ".format(floor,room), end="")
        else:
            print("A{0}{1} ".format(floor,room), end="")
    print()