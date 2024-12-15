print('MENGURUTKAN KATA SESUAI ABJAD')

kata = str(input('\nMasukkan kata, gunakan spasi\nuntuk memisahkan (contoh : a i r q) : \n'))

daftar = kata.split()
daftar.sort()

urut = ' '.join(daftar)

print(f"Urutan sesuai abjad : {urut}")