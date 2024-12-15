pilihan = input("Pilih jenis senjata (Assault/Sniper/Pistol) : ")

assault = ["AK","M4A1","SCAR","Groza","FAMAS","AUG""AN94","M14"]
sniper = ["AWM","M82B","KAR98K"]
pistol = ["M1917","M500","M1873","Hand-Cannon","USP","G18"]
pilihan = pilihan.lower()

if pilihan == "assault":
    print("\nSenjata jenis Assault Rifle")
    print(assault)

elif pilihan == "sniper":
    print("\nSenjata jenis Sniper Rifle")
    print(sniper)

elif pilihan == "pistol":
    print("\nSenjata jenis Pistol")
    print(pistol)
else:
    print("\nInputan salah. Coba lagi")