flowers = input()
num_flowers=int(input())
budget=int(input())

end_price=0

if flowers=="Roses":
    end_price=num_flowers*5
    if num_flowers>80:
        end_price *=0.90
elif flowers=="Dahlias":
    end_price=num_flowers*3.80
    if num_flowers>90:
        end_price *=0.85
elif flowers=="Tulips":
    end_price= num_flowers*2.80
    if num_flowers>80:
        end_price *=0.85
elif flowers=="Narcissus":
    end_price = num_flowers * 3
    if num_flowers<120:
        end_price *=1.15
elif flowers=="Gladiolus":
    end_price = num_flowers * 2.50
    if num_flowers<80:
        end_price *=1.20

difference = abs(budget-end_price)

if end_price<=budget:
    print(f"Hey, you have a great garden with {num_flowers} {flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")



