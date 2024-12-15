print("Menghitung berapa Minggu\nuntuk kamu mencapai umur 80")

def umur(usia):
    hariHidup = int(usia * 365)
    mingguHidup = round(int(hariHidup /7))
    totalMinggu = round(int((80 * 365)/7))
    output = totalMinggu - mingguHidup
    print(f"Kamu mempunyai {output} minggu lagi untuk mecapai umur 80")

umur(int(input('Masukkan umur kamu:(Hanya angka)')))