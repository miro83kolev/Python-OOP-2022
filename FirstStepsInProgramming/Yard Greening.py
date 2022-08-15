square_meters = float(input())
total_yard_price = square_meters*7.61
total_discount = total_yard_price*0.18
final_sum = total_yard_price-total_discount

print(f'The final price is: {final_sum} lv.')
print(f'The discount is: {total_discount} lv.')
