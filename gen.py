tahun = int(input('Input tahun lahir kamu:\n'))
if tahun > 1980 and tahun < 1997:
    print("Kamu adalah gen Millenial.")
elif tahun >= 1997 and tahun < 2012:
    print("Kamu adalah gen Z.")
elif tahun >=2012 and tahun < 2024:
    print("Kamu adalah gen Alpha.")

    
umur =2024 - tahun
print(f"Umur kamu {umur} tahun")
if umur >= 17:
    print(f"Kamu sudah bisa mengemudi di umur {umur} tahun")
elif umur < 17:
    print(f"Kamu belum bisa mengemudi di umur {umur} tahun")