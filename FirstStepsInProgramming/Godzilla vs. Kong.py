budget = float(input())
people = int(input())
price_clothes = float(input())

decor = budget*0.10
total_sum_clothes = people*price_clothes
if people>=150:
    total_sum_clothes *=0.90

total_movie_amount = decor+total_sum_clothes

if total_movie_amount<=budget:
    print("Action!")
    print(f"Wingard starts filming with {(budget-total_movie_amount):.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {(total_movie_amount-budget):.2f} leva more.")
