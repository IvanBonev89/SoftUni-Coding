def software_version(soft_ver):
    version = [int(digit) for digit in soft_ver]
    version[-1] += 1
    for index in range(len(version)-1, -1,-1):
        if version[index] > 9:
            version[index] = 0
            if index - 1 >= 0:
                version[index-1] += 1
    return version



soft_ver = input().split(".")
result = software_version(soft_ver)
print(f"{result[0]}.{result[1]}.{result[2]}")
#print(".".join(str(number) for number in result))

