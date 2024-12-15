import random
logo ='''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

def acak():
    list_barangLelang = ["Mobil BKW","Lamborghini Prison","Sepatu Messi"]

    barangDilelang =random.randint(1,4)
    print(f"Barang yang akan di lelang {barangDilelang}")


Tawar ={}
TawarFinish = False
def hargaTertinggi(biddingrecord):
    hargaTertinggi = 0
    pemenang = ""
    for x in biddingrecord:
        jumlahTawar = biddingrecord[x]
        if jumlahTawar > hargaTertinggi:
            hargaTertinggi = jumlahTawar
            winner = x
    print(f"Pemenangnya adalah {winner} dengan tawaran Rp.{hargaTertinggi}")
while not TawarFinish:
    nama = input("Siapa nama kamu? ")
    harga = int(input("Ingin taruh harga berapa? "))
    Tawar[nama] = harga
    harus_lanjut = input("Apakah ada penawar lain? 'Ketik' ya atau 'tidak'.\n")
    if harus_lanjut == "no":
        TawarFinish = True
        hargaTertinggi(Tawar)
    elif harus_lanjut == "Yes":
        TawarFinish = True

acak()