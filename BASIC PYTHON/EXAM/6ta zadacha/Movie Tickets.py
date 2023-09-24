a1 = int(input())
a2 = int(input())
n = int(input())
nn = int(n / 2)
sym2 = 0
for symbol_1 in range(a1, a2):
    if symbol_1 % 2 != 0:
        sym = chr(symbol_1)
        for symbol_2 in range(1, n):

                sym2 = symbol_2
                for symbol_3 in range(1, nn):

                        sym3 = symbol_3
                        sym4 = ord(sym)
                        if (sym2 + sym3 + sym4) % 2 != 0:
                            print(f'{sym}-{sym2}{sym3}{sym4}')
