weidth=int(input())
lenght=int(input())
cake_pieces = weidth*lenght

inpt=input()
while inpt !='STOP':
    current_pieces=int(inpt)
    cake_pieces -=current_pieces

    if cake_pieces<=0:
        break
    inpt = input()

if cake_pieces>0:
    print(f'{cake_pieces} pieces are left.')
else:
    print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')