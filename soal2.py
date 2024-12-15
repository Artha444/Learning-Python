nama_barang = input('Nama barang\t: ').lower()
jumlah_barang = int(input('Jumlah barang\t: '))

harga_kertas = 1000

if nama_barang == 'kertas':
    if jumlah_barang >= 20:
        ketersediaan = False
    else:
        ketersediaan = True

total = harga_kertas * jumlah_barang

print('~'*30)
print('Nama barang\t: ',nama_barang)
print('Jumlah barang\t: ',jumlah_barang)
print('Harga\t\t: Rp.',total)
print(f'Ketersediaan\t: {ketersediaan}')