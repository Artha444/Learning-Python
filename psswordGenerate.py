import random

input = input("Kata sandi random untuk anda ('ya' atau 'tidak')\ninput : ").lower

if input == 1 or "Ya":
    jmlhkataSandi = 16
    angka_kata = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    kataSandi = ""

    for x in range(jmlhkataSandi):
        kataSandi = kataSandi + random.choice(angka_kata)


    print("\nkata sandi untuk anda : {}".format(kataSandi))
else:
    print('baiklah')