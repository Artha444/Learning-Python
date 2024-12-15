print('='*20)
print('MENENTUKAN USIA')

u = int(input('Masukkan umur : '))

if u > 0 and u < 6:
    print('Usia balita')
elif u > 5 and u < 14:
    print('Usia anak-anak')
elif u > 13 and u < 25:
    print('Usia remaja')
elif u > 24:
    print('Usia tua')
else:
    print('Inputan salah, coba lagi.')