print("Menghitung jumlah huruf Vokal pada kalimat")

kalimat = input('Masukkan kalimat : ')

vokal = "aiueoAIUEO"
jumlahVokal = sum(1 for char in kalimat if char in vokal)

print(f"\n'{kalimat}', kalimat ini memiliki huruf vokal sebanyak : {jumlahVokal}")