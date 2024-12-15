print("KONVERTER DARI DESIMAL KE BINER\n")

angka = int(input("Masukkan angka desimal: "))
biner = bin(angka)

print(f"{"="*30}\n\tHasil Konversi\n{"="*30}\n\nDesimal\t: {angka}\nBiner\t: {biner[2:]}")