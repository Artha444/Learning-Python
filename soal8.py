print('='*20)
print('DISKON BARANG')
print('='*20)

list_barang =  ['Baju\t\t: 23.000','Celana\t: 16.000']

print('List dan harga Satuan Barang')
print('Minimal pembelian 100.000 untuk mendapat 5% diskon')
print('Minimal pembelian 80.000 untuk mendapat 4% diskon')
for x,y in enumerate(list_barang):
    print(f'{x+1}. {y}')
print('='*20)
barang = int(input('No barang\t\t: '))
jumlah = int(input('Jumlah barang\t\t: '))

print('='*15)

if barang == 1:
    harga = 23000 * jumlah
    print('Harga\t\t\t:',harga)
    if harga  > 100000:
        mendapat_diskon = True
        diskon = harga * 0.5
        bulat = round(diskon)
        print('Mendapat diskon\t\t:',mendapat_diskon)
        print('Diskon\t\t\t: 5 %')
        print('Harga\t\t\t:',harga)
        print('Hasil setelah diskon\t:',bulat)
    else :
        mendapat_diskon = False
        print('Mendapat diskon\t\t:',mendapat_diskon)

if barang == 2:
    harga = 16000 * jumlah
    print('Harga\t\t\t:',harga)
    if harga > 80000:
        diskon = harga * 0.4
        bulat = round(diskon)
        mendapat_diskon = True
        print('Mendapat diskon\t\t:',mendapat_diskon)
        print('Diskon\t\t\t: 4 %')
        print('Hasil setelah diskon\t:',bulat)
    else :
        mendapat_diskon = False
        print('Mendapat diskon\t\t:',mendapat_diskon)