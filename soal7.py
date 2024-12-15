asal = ['Indonesia','Malaysia','Bekasi']
kel = ['Team 1','Team 2','Team 3']

print('~'*21)
print('Pilih antara (1 - 3):')
print('~'*21)
print('Team')

for a,b in enumerate(kel):
    print(f'{a+1}. {b}')
print('='*16)

iKel = int(input('Kelompok : '))


print('~'*21)
print('Pilih antara (1 - 3):')
print('~'*21)
print('Daerah')

for x,y in enumerate(asal):
    print(f'{x+1}. {y}')
print('='*16)

iAsal = int(input('Asal daerah : '))


print('-')
if iKel == 1:
    print('Kelompok    :',kel[0])
elif iKel == 2:
    print('Kelompok    :',kel[1])
elif iKel == 3:
    print('Kelompok    :',kel[2])

if iAsal == 1:
    print('Asal daerah :',asal[0])
    print('Jumlah tim  : 29 orang')
elif iAsal == 2:
    print('Asal daerah :', asal[1])
    print('Jumlah tim  : 31 orang')
elif iAsal == 3:
    print('Asal daerah :',asal[2])
    print('Jumlah tim  : 9 orang')