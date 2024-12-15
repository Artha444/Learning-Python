print('='*30)
print('   HURUF VOKAL DAN KONSONAN')
print('='*30)

x = str(input('Masukkan huruf : ')).lower()

if x == 'a' or x == 'i' or x == 'u' or x == 'e' or x == 'o':
    print('Huruf vokal')

elif x == 'b' or x == 'c' or x == 'd' or x == 'f' or x == 'g' or x == 'h' or x == 'j' or x == 'k' or x == 'l' or x == 'm' or x == 'n' or x == 'o' or x == 'p' or x == 'q' or x == 'r' or x == 's' or x == 't' or x == 'u' or x == 'v' or x == 'y' or x == 'z':
    print('Huruf konsonan')

else:
    print(x,'Bukan huruf.')