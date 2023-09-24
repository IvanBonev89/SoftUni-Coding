nylon = int(input())
paint = int(input())
paint_r = int(input())
hours = int(input())


price_nylon = 1.50
price_paint = 14.50
price_paint_r = 5.00
price_bags = 0.40

total_nylon = nylon + 2
total_paint = paint * 1.1

total_price = (total_nylon*price_nylon) + (total_paint*price_paint) + (paint_r*price_paint_r) + price_bags
percent_from_total = total_price * 0.3
cost_worker = hours * percent_from_total
total = total_price+cost_worker
print("сумата на всички разходи")
print(total)




