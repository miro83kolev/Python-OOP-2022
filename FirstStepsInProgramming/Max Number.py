import sys

inpt = input()

maxNum = -sys.maxsize

while inpt !="Stop":
    num = int(inpt)

    if num>maxNum:
        maxNum=num
    inpt = input()

print(maxNum)