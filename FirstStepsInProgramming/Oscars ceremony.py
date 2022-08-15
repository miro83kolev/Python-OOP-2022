rent = int(input())

statues = rent*0.70
catering = statues*0.85
sound_equipment = catering/2

total_expenses = rent+statues+catering+sound_equipment
print(f'{total_expenses:.2f}')