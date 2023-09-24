length = int(input())
width = int(input())
height = int(input())
percent_area = int(input())
percent_area_int = percent_area/100
area = length*width*height
area_liters = area * 0.001
free_area = area_liters*(1-percent_area_int)
print(free_area)



