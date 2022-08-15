budget = int(input())
season = input()
fishermans = int(input())

boat_rent=0

if season=="Spring":
    boat_rent=3000
    if fishermans<=6:
        boat_rent *=0.90
    elif fishermans>=7 and fishermans<=11:
        boat_rent *=0.85
    elif fishermans>=12:
        boat_rent *=0.75
if season=="Summer" or season=="Autumn":
    boat_rent=4200
    if fishermans<=6:
        boat_rent *=0.90
    elif fishermans>=7 and fishermans<=11:
        boat_rent *=0.85
    elif fishermans>=12:
        boat_rent *=0.75
if season=="Winter":
    boat_rent=2600
    if fishermans<=6:
        boat_rent *=0.90
    elif fishermans>=7 and fishermans<=11:
        boat_rent *=0.85
    elif fishermans>=12:
        boat_rent *=0.75

if fishermans %2==0 and season !="Autumn":
    boat_rent *=0.95

difference = abs(budget-boat_rent)

if budget>=boat_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")