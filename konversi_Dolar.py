print(f"{"="*30}\nKonversi mata uang Rupiah ke Dolar\n{"="*30}\n")

Dolar = float(input("Masukkan Jumlah Dalam Mata Uang Dolar : "))

kurs = 15000
Rupiah = Dolar * kurs

print(f"\n${Dolar:.0f} di konversi menjadi Rp.{Rupiah:.0f}")