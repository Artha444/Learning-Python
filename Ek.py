m = float(input('Massa benda\t: '))
v = float(input('Kecepatan benda\t: '))

Ek = 1/2 * m * v **2

if Ek >= 1000:
    Ek1 = Ek / 1000
    print('Hasilnya adalah\t: ',Ek,'J')
    print('Hasilnya adalah\t: ',Ek1,'J')