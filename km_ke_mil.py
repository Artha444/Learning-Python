def km_ke_mil(km):
    mil = km * 0.621371
    return mil

k = float(input("Masukkan jarak kilometer : "))
konversi = km_ke_mil(k)
print(f"{k} km dikonversikan ke mil menjadi : {konversi}")