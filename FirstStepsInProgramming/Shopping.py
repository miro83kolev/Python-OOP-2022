peters_budget = float(input())
gpus = int(input())
processors = int(input())
rams = int(input())

gpus_price = gpus*250
processors_price = (gpus_price*0.35)*processors
rams_price = (gpus_price*0.10)*rams
total_price = gpus_price+processors_price+rams_price

if gpus>processors:
    total_price *=0.85

difference = abs(peters_budget-total_price)
if total_price<=peters_budget:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")