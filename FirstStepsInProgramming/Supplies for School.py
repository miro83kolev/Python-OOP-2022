pen_packs = int(input())
markers_packs = int(input())
detergent_litters = int(input())
discount = int(input())

price_pens = pen_packs*5.80
price_markers = markers_packs*7.20
price_detergent = detergent_litters*1.20
converted_discount = discount/100
total_materials = price_pens+price_markers+price_detergent
price_with_discount = total_materials-(total_materials*converted_discount)
print(price_with_discount)