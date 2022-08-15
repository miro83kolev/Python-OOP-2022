destination=input()

while destination !="End":
    cost = float(input())
    total_savings=0

    while cost>total_savings:
        saving=float(input())
        total_savings +=saving
    print(f'Going to {destination}!')
    destination=input()