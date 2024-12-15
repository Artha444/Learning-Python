print(f"{"-"*30}\nTranslate Huruf Hijaiyah\n{"-"*30}")

huruf = str(input("Masukkan kata (contoh : alif/ba/tsa) : "))
huruf = huruf.lower()

if huruf == "alif":
    hijaiyah = "ا"
    print(f"kata '{huruf}' dalam huruf hijaiyah adalah {hijaiyah}")

elif huruf == "ba":
    hijaiyah = "ب"
    print(f"kata '{huruf}' dalam huruf hijaiyah adalah {hijaiyah}")

elif huruf == "ta":
    hijaiyah = "ت"
    print(f"kata '{huruf}' dalam huruf hijaiyah adalah {hijaiyah}")

elif huruf == "tsa":
    hijaiyah = "ث"
    print(f"kata '{huruf}' dalam huruf hijaiyah adalah {hijaiyah}")

elif huruf == "jim":
    hijaiyah = "ج"
    print(f"kata '{huruf}' dalam huruf hijaiyah adalah {hijaiyah}")

elif huruf == "ha":
    hijaiyah = "ج"
    print(f"kata '{huruf}' dalam huruf hijaiyah adalah {hijaiyah}")

elif huruf == "kho":
    hijaiyah = "خ"
    print(f"kata '{huruf}' dalam huruf hijaiyah adalah {hijaiyah}")

elif huruf == "dal":
    hijaiyah = "د"
    print(f"kata '{huruf}' dalam huruf hijaiyah adalah {hijaiyah}")

elif huruf == "dzal":
    hijaiyah = "ذ"
    print(f"kata '{huruf}' dalam huruf hijaiyah adalah {hijaiyah}")

elif huruf == "ro":
    hijaiyah = "ر"
    print(f"kata '{huruf}' dalam huruf hijaiyah adalah {hijaiyah}")

else:
    print('Inputan valid. Atau huruf arab belum di program')