skumriq_price = float(input())
caca_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())
palamud_price = skumriq_price * 1.6
safrid_price = caca_price * 1.8
total_midi_price = midi_kg * 7.50
total_palamud_price = palamud_kg * palamud_price
total_safrid_price = safrid_kg * safrid_price
total_price = total_safrid_price + total_palamud_price + total_midi_price
print(f"{total_price:.2f}")




