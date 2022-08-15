needed_nylon = int(input())
needed_paint = int(input())
needed_detergent = int(input())
needed_hours = int(input())

sum_nylon = (needed_nylon+2)*1.50
sum_paint = ((needed_paint+needed_paint*0.1))*14.50
sum_detergent = needed_detergent*5
sum_bags=0.40
total_sum = sum_nylon+sum_paint+sum_detergent+sum_bags
sum_workers = (total_sum*0.30)*needed_hours
final_sum = total_sum+sum_workers

print(final_sum)