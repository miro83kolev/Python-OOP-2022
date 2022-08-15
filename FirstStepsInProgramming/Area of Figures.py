import math

figure = str(input())

area=0
if figure=='square':
    side =float(input())
    area=side*side
    print(f"{area:.3f}")
elif figure=='rectangle':
    sideA=float(input())
    sideB=float(input())
    area=sideA*sideB
    print(f"{area:.3f}")
elif figure=="circle":
    side = float(input())
    area = side*side*math.pi
    print(f"{area:.3f}")
elif figure=='triangle':
    sideA = float(input())
    sideB = float(input())
    area = (1/2)*sideA*sideB
    print(f"{area:.3f}")

