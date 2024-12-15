print(f"{"-"*18}\nFREKUENSI KARAKTER\n{"-"*18}")

kata = str(input('Masukkan kalimat : '))
fre = {}

for y in kata:
    if y in fre:
        fre[y] += 1
    else:
        fre[y] = 1

print("Frekuensi karakternya adalah :",fre)