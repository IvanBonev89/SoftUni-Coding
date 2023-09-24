num = int(input())

for first_symbol in range(num):
    for second_symbol in range(num):
        for trird_symbol in range(num):
            result =(f"{chr(97+first_symbol)}{chr(97+second_symbol)}{chr(97+trird_symbol)}")
            print(result)