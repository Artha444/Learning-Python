op1 = float(input('Masukkan angka\t: '))
op2 = input('(+ , - , x , /)\t: ')
op3 = float(input('Masukkan angka\t: '))

if op2 == '+':
    hasil = op1 + op3

elif op2 == '-':
    hasil = op1 - op3

elif op2 == 'x':
    hasil = op1 * op3

elif op2 == '/':
    hasil = op1 / op3

else:
    print('Inputan error, mohon coba lagi')
    
print(f"{"="*20}\nHasilnya adalah : {hasil}")