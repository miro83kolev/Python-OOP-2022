tax = int(input())

price_basketball_sneakers = tax*0.60
price_basketball_jersey = price_basketball_sneakers*0.80
price_basketball_ball = price_basketball_jersey/4
price_basketball_accessories = price_basketball_ball/5
final_amount = tax+price_basketball_sneakers+price_basketball_jersey+price_basketball_ball+price_basketball_accessories

print(round(final_amount,2))

