print('='*30)
print('RUMUS KECEPATAN')
print('='*30)

s = int(input(f'Input jarak / perpindahan\t(km) : '))
t = int(input('Input waktu\t(jam) : '))

konversi_km_ke_m = s * 1000
konversi_jam_ke_s = t * 3600
v = konversi_km_ke_m / konversi_jam_ke_s
print(v,'m/s')