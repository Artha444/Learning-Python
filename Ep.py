print('='*20)
print('  ENERGI POTENSIAL')
print('='*20)

print('g = 10m/s')

m = float(input('Massa benda\t\t: '))
h = float(input('Ketinggian benda\t: '))

g = 10  #10m/s

Ep = m * g * h
if Ep >= 1000:
    ep1 = Ep / 1000
    print('Hasilnya adalah\t: ',Ep,'kJ')
    print('Dikonversikan menjadi\t:',ep1,'J')
else:
    print('Hasilnya adalah\t: ',Ep,'J')