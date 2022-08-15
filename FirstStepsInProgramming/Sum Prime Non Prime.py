inpt=input()

sum_prime=0
sum_noprime=0

while inpt !="stop":
    is_prime = True
    number = int(inpt)

    if number<0:
        number=0
        print('Number is negative.')
    elif number==1:
        is_prime=False
    else:
        for count in range(2, number+1):
            if number%count==0 and count !=number:
                is_prime=False
                break

    if is_prime:
        sum_prime +=number
    else:
        sum_noprime +=number
    inpt = input()

if inpt=="stop":
    print(f'Sum of all prime numbers is: {sum_prime}')
    print(f'Sum of all non prime numbers is: {sum_noprime}')