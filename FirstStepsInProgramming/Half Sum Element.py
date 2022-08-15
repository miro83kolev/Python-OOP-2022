import sys

n = int(input())

max_num = -sys.maxsize
sum=0

for i in range(n):
    num = int(input())
    sum += num
    if num > max_num:
        max_num = num

sum -=max_num

if sum==max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    sum_others=max_num-sum
    print('No')
    print(f'Diff = {abs(sum_others)}')