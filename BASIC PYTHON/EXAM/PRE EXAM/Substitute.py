# input

k = int(input())
l = int(input())
m = int(input())
n = int(input())
num1 = ''
num2 = ''
num3 = ''
num4 = ''
count = 0
for i in range(k, 8 + 1):

    for ii in range(9, l - 1, -1):

        for j in range(m, 8 + 1):

            for jj in range(9, n - 1, -1):

                if i % 2 == 0:
                    num1 = i
                    if ii % 2 != 0:
                        num2 = ii
                        if j % 2 == 0:
                            num3 = j
                            if jj % 2 != 0:
                                num4 = jj
                                num1_s = str(num1)
                                num2_s = str(num2)
                                num3_s = str(num3)
                                num4_s = str(num4)
                                total_num = (num1_s)+(num2_s)
                                total_num2 = (num3_s)+(num4_s)
                                if (total_num != total_num2):
                                    count += 1
                                    print(f"{num1}{num2} - {num3}{num4}")
                                else:
                                    print("Cannot change the same player.")
                                if count >= 6:
                                    exit()
