excursion = float(input())
puzzels = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

sum_all_toys=puzzels*2.60+dolls*3+bears*4.10+minions*8.20+trucks*2
num_all_toys = puzzels+dolls+bears+minions+trucks

if num_all_toys>=50:
    sum_all_toys *=0.75

rent = sum_all_toys*0.10
profit = sum_all_toys-rent
difference = abs(excursion-profit)

if  profit>=excursion:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")