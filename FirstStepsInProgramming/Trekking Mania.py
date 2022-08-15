number_of_groups = int(input())

group1=0
group2=0
group3=0
group4=0
group5=0
total_climbers=0

for i in range(number_of_groups):
    num_of_climbers = int(input())

    if num_of_climbers<=5:
        group1 +=num_of_climbers
        total_climbers +=num_of_climbers
    elif num_of_climbers >=6 and num_of_climbers<=12:
        group2 += num_of_climbers
        total_climbers += num_of_climbers
    elif num_of_climbers >= 13 and num_of_climbers <= 25:
        group3 += num_of_climbers
        total_climbers += num_of_climbers
    elif num_of_climbers >= 26 and num_of_climbers <= 40:
        group4 += num_of_climbers
        total_climbers += num_of_climbers
    elif num_of_climbers >= 41:
        group5 += num_of_climbers
        total_climbers += num_of_climbers

group1_percentage=group1/total_climbers*100
group2_percentage=group2/total_climbers*100
group3_percentage=group3/total_climbers*100
group4_percentage=group4/total_climbers*100
group5_percentage=group5/total_climbers*100

print(f'{group1_percentage:.2f}%')
print(f'{group2_percentage:.2f}%')
print(f'{group3_percentage:.2f}%')
print(f'{group4_percentage:.2f}%')
print(f'{group5_percentage:.2f}%')
