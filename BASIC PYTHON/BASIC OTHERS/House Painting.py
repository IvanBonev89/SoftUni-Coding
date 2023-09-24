x = float(input())
y = float(input())
h = float(input())
s_kvadrat = x*x
s_pravoagalnik = x * y
s_triagalnik = (x*h)/2
s_vrata = 2 * 1.2
s_prozorec = 1.5 * 1.5
area_preden_kvadrat = s_kvadrat - s_vrata
area_stranichen_pravoagalinik = s_pravoagalnik - s_prozorec
area_green = s_kvadrat + area_preden_kvadrat + area_stranichen_pravoagalinik + area_stranichen_pravoagalinik
area_red = s_pravoagalnik + s_pravoagalnik + s_triagalnik + s_triagalnik
green_paint = area_green/3.4
red_paint = area_red/4.3
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
