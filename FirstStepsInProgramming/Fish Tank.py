length = int(input())
weidth = int(input())
height = int(input())
percent = float(input())

volume = length*weidth*height
volume_litters=volume/1000
space_percentage = percent/100
needed_litters=volume_litters*(1-space_percentage)
print(needed_litters)