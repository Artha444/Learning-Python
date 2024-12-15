print(f"{"-"*30}\n\tFAKTORIAL\n{"-"*30}")

angka = int(input('Masukkan angka : '))

faktorial = 1

if angka < 0:
    print("Coba lagi. Kurang dari 0, program mencetak pesan bahwa faktorial tidak terdefinisi untuk bilangan negatif.")

elif angka == 0:
    print("Faktorial 0 adalah 1")

else:
    for x in range(1,angka + 1):
        faktorial *= x
        print(f"Faktorial dari {angka} adalah {faktorial}")