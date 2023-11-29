import re
number_barcode = int(input())
barcode_is_valid = False
product_group = ''
for i in range(1, number_barcode+1):
    barcode = input()
    pattern = r"@[#]+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
    matches = re.findall(pattern,barcode)
    if matches:
        barcode_is_valid = True
        for code in matches:
            list_code = list(code)
            for symbol in list_code:
                if not symbol.isdigit():
                    pass
                else:
                    product_group += symbol
            if product_group:
                print(f"Product group: {product_group}")
            else:
                product_group = '00'
                print(f"Product group: {product_group}")
        product_group = ''
    else:
        print("Invalid barcode")
