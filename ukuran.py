print('='*30)
print('UKURAN SEPATU')
print('='*30)

a = int(input('Masukkan nomor sepatu:'))

if a > 29 and a <36:
    print('Ukuran sepatu kecil')
elif a > 35 and a <41:
    print('Ukuran sepatu sedang')
elif a >40 and a < 46:
    print('Ukuran sepatu besar')

else:
    print('Inputan salah, coba lagi')