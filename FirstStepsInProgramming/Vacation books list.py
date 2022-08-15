pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_book_time=float(pages/pages_per_hour)
total_hours_per_day = round(total_book_time/days)
print(total_hours_per_day)