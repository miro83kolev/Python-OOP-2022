deposit = float(input())
months = int(input())
interest = float(input())

interest_total = deposit*(interest/100)
interest_month = interest_total/12
total_amount=deposit+(months*interest_month)
print(total_amount)