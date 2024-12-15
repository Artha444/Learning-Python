print("ANGKA PRIMA")

angka = int(input("Masukkan angka(jumlah angka hanya satu) : "))

prima = True
if((angka == 0) or (angka == 1)):
    prima = False
else:
    for x in range(2,(angka//2)):
        if((angka % x) == 0):
            prima = False
            break

    if(prima):
        print(f"\nAngka {angka} adalah angka prima")
    else:
        print(f"\nAngka {angka} bukan angka prima")