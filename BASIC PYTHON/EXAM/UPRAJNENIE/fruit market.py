price_strawbery = float(input())
quant_banana = float(input())
quant_oragne = float(input())
quant_malini = float(input())
quant_strawbery = float(input())
money = 0
total_strawbery = price_strawbery * quant_strawbery
price_malini = 0.5 * price_strawbery
total_malini = price_malini * quant_malini
price_orange = price_malini - (0.4 * price_malini)
total_orange = price_orange * quant_oragne
price_banana = price_malini - (price_malini * 0.8)
total_banana = price_banana * quant_banana
money = total_banana + total_orange + total_malini + total_strawbery
print(f"{money:.2f}")
