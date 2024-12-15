print("BULAN LANGKA")

bulan1 = ["Januari","Februari","Mei"]
bulan2 = ["Maret","April","Juni","Juli","November","Desember"]
bulan3 = ["September","Agustus","Oktober"]

print("\nBulan langka\t:")
for x,y in enumerate(bulan1):
    print(x+1,'.',y)
print("\nBulan umum\t:")
for k,l in enumerate(bulan2):
    print(k+1,'.',l)
print("\nBulan populer\t:")
for m,n in enumerate(bulan3):
    print(m+1,'.',n)