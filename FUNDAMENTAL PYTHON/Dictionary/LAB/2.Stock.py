info = input().split()
search_products = input().split()
stock = {}

for i in range(0,len(search_products)):
    product = search_products[i]

    if search_products[i] in info:
        for j in range(0,len(info),2):
            quantity = info[j + 1]
            if search_products[i] == info[j]:
                 print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
