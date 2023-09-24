#from math import ceil
peoples = int(input())
max_peoples = int(input())
counter = 0
for i in range (1,peoples+1):
    counter += max_peoples
    if counter < peoples:
        continue
    else:
        break
cycle = counter / max_peoples
print(int(cycle))


# vtori nachin

#courses = ceil(peoples / max_peoples)

