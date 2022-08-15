city = input()
sales = float(input())

commission_amount=0

if city=="Sofia":
    if sales >=0 and sales <=500:
        commission_amount=sales*0.05
        print(f"{commission_amount:.2f}")
    elif sales>500 and sales<=1000:
        commission_amount=sales*0.07
        print(f"{commission_amount:.2f}")
    elif sales > 1000 and sales <= 10000:
        commission_amount = sales * 0.08
        print(f"{commission_amount:.2f}")
    elif sales >10000:
        commission_amount = sales * 0.12
        print(f"{commission_amount:.2f}")
    else:
        print("error")
elif city=="Varna":
    if sales >=0 and sales <=500:
        commission_amount=sales*0.045
        print(f"{commission_amount:.2f}")
    elif sales>500 and sales<=1000:
        commission_amount=sales*0.075
        print(f"{commission_amount:.2f}")
    elif sales > 1000 and sales <= 10000:
        commission_amount = sales * 0.10
        print(f"{commission_amount:.2f}")
    elif sales >10000:
        commission_amount = sales * 0.13
        print(f"{commission_amount:.2f}")
    else:
        print("error")
elif city=="Plovdiv":
    if sales >= 0 and sales <= 500:
        commission_amount = sales * 0.055
        print(f"{commission_amount:.2f}")
    elif sales > 500 and sales <= 1000:
        commission_amount = sales * 0.08
        print(f"{commission_amount:.2f}")
    elif sales > 1000 and sales <= 10000:
        commission_amount = sales * 0.12
        print(f"{commission_amount:.2f}")
    elif sales > 10000:
        commission_amount = sales * 0.145
        print(f"{commission_amount:.2f}")
    else:
        print("error")
else:
    print("error")