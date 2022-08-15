movie_name = input()
hall_type = input()
tickets = int(input())

income = 0

if movie_name =="A Star Is Born":
    if hall_type=="normal":
        income= tickets*7.50
    elif hall_type=="luxury":
        income = tickets * 10.50
    elif hall_type == "ultra luxury":
        income = tickets * 13.50
elif movie_name=="Bohemian Rhapsody":
    if hall_type == "normal":
        income = tickets * 7.35
    elif hall_type == "luxury":
        income = tickets * 9.45
    elif hall_type == "ultra luxury":
        income = tickets * 12.75
elif movie_name=="Green Book":
    if hall_type == "normal":
        income = tickets * 8.15
    elif hall_type == "luxury":
        income = tickets * 10.25
    elif hall_type == "ultra luxury":
        income = tickets * 13.25
elif movie_name=="The Favourite":
    if hall_type == "normal":
        income = tickets * 8.75
    elif hall_type == "luxury":
        income = tickets * 11.55
    elif hall_type == "ultra luxury":
        income = tickets * 13.95

print(f'{movie_name} -> {income:.2f} lv.')