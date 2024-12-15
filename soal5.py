print('='*37)
print('ANGKA TERKECIL DAN ANGKA TERBESAR')
print('='*37)
x = int(input('Angka 1 : '))
y = int(input('Angka 2 : '))
z = int(input('Angka 3 : '))

print('~'*20)
if x > y and x > z:
    print(x,'adalah angka terbesar')
elif y > z and y > x:
    print(y,'adalah angka terbesar')
elif z > y and z > x:
    print(z,'adalah angka terbesar')
if x < y and x < z:
    print(x,'adalah angka terkecil')
elif y < z and y < x:
    print(y,'adalah angka terkecil')
elif z < y and z < x:
    print(z,'adalah angka terkecil')