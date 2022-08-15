chicken_menu=int(input())
fish_menu=int(input())
veggie_menu=int(input())
delivery = 2.50

sum_chicken = chicken_menu*10.35
sum_fish = fish_menu*12.40
sum_veggie = veggie_menu*8.15
total_all_menus = sum_chicken+sum_fish+sum_veggie
price_desert = total_all_menus*0.20
final_amount=total_all_menus+delivery+price_desert

print(round(final_amount,2))
