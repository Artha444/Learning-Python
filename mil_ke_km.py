def mil_ke_km(mil):
    km = mil * 1.60934
    return km

m = float(input("Masukkan jarak mil : "))
konversi = mil_ke_km(m)
print(f"{m} mil dikonversikan ke km menjadi : {konversi}")
