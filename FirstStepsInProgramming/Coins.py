money=float(input())
money=round(money*100)
counter = 0

while money>0:
    if money>=200:
        counter +=1
        money -=200
    elif money>=100:
        counter +=1
        money -=100
    elif money >= 50:
        counter += 1
        money -= 50
    elif money >= 20:
        counter += 1
        money -= 20
    elif money >= 10:
        counter += 1
        money -= 10
    elif money >= 5:
        counter += 1
        money -= 5
    elif money >= 2:
        counter += 1
        money -= 2
    elif money >= 1:
        counter += 1
        money -= 1
    else:
        break

print(counter)