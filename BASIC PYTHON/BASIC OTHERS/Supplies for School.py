himikali = int(input())
markeri = int(input())
preparat = int(input())
discount = int(input())

discount_2 = float(discount/100)
cost_himikali = 5.80 * himikali
cost_markeri = 7.20 * markeri
cost_preparat = 1.20 * preparat

total_cost = cost_himikali+cost_markeri+cost_preparat
total_cost_with_discount = total_cost - (total_cost*discount_2)
print(total_cost_with_discount)





