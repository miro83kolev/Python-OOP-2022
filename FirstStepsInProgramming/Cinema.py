movie_type=input()
rows = int(input())
colums = int(input())

income=0
cinema_capacity=rows*colums

if movie_type=="Premiere":
    income=cinema_capacity*12
elif movie_type=="Normal":
    income = cinema_capacity * 7.50
elif movie_type=="Discount":
    income = cinema_capacity * 5

print(f"{income:.2f} leva")