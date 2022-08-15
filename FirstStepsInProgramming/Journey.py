budget = float(input())
season = input()

destination=""
type=""
price=0

if budget<=100:
    destination="Bulgaria"
    if season=="summer":
        type="Camp"
        price = budget*0.30
    elif season=="winter":
        type="Hotel"
        price=budget*0.70
elif budget<=1000:
    destination="Balkans"
    if season=="summer":
        type="Camp"
        price = budget*0.40
    elif season=="winter":
        type="Hotel"
        price=budget*0.80
elif budget>1000:
    destination="Europe"
    if season == "summer":
        type = "Hotel"
        price = budget * 0.90
    elif season == "winter":
        type = "Hotel"
        price = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{type} - {price:.2f}")