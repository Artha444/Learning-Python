import math
print(f"{"-"*35}\nKonsep dasar matematika KPK dan FPB\n{"-"*35}")

angka1 = int(input('Masukkan angka pertama : '))
angka2 = int(input('Masukkan angka kedua   : '))

fpb = math.gcd(angka1,angka2)
kpk = (angka1 * angka2) // fpb
print(f"\nFPB dari {angka1} dan {angka2} adalah {fpb}")
print(f"KPK dari {angka1} dan {angka2} adalah {kpk}")