import random

print(f"{"="*35}\nGACHA BERKESEMPATAN MENDAPATAN TAS\n{"="*35}")

angka = int(input('Masukkan jumlah gacha (angka 1 atau 5)\ninput angka : '))

def gacha():
    if angka == 5:
        list_hadiah=["Casing HP","Botol minum","Tas","Headset"]

        hasil_gacha = random.randint(1,5)

        hadiah = random.randint(20000, 40000)
        barang_random = random.choice(list_hadiah)

        if hasil_gacha ==3:
            print(f"| |\n| |\n| |Anda mendapatkan hadiah Rp.{hadiah}\n| |\n| |")
        else:
            print(f"| |\n| |\n| |Anda mendapatkan {barang_random}\n| |\n| |")
    
    elif angka == 1:
        list_hadiah=["Zonk","Botol minum","Tas","Zonk"]

        hasil_gacha = random.randint(1,5)

        hadiah = random.randint(5000, 10000)
        barang_random = random.choice(list_hadiah)

        if hasil_gacha ==3:
            print(f"| |\n| |\n| |Anda mendapatkan hadiah Rp.{hadiah}\n| |\n| |")
        else:
            print(f"| |\n| |\n| |Anda mendapatkan {barang_random}\n| |\n| |")
    else:
        print("Inputan Invalid. Mohon coba lagi")



gacha()