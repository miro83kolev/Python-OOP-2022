age = int(input())
washing_machine_price = float(input())
toys_price = int(input())

money=0
toys=0
years=0
saved_money=0

for birthdays in range(1, age+1):
    if birthdays%2==0:
        money += 10 + (toys-1)*10
        years +=1
    else:
        toys +=1

saved_money = (money-years)+(toys*toys_price)
if saved_money >= washing_machine_price:
    print(f'Yes! {saved_money - washing_machine_price:.2f}')
else:
    print(f'No! {washing_machine_price - saved_money:.2f}')