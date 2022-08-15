import sys

inpt = input()

minNum = sys.maxsize

while inpt !="Stop":
    num = int(inpt)

    if num<minNum:
        minNum=num
    inpt = input()

print(minNum)