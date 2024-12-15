print("Mengkonversi Suhu Reamur")

reamur = int(input('Masukkan Suhu Reamurnya : '))

celcius = (5/4) * reamur
fahrenheit = (9/4 * reamur) + 32
kelvin = (5/4 * reamur) + 273

print(f"\n{reamur}°R\n{"-"*20}\nDIKONVERSIKAN\n{"-"*20}")
print(f"Celcius Menjadi\t\t: {celcius}°C")
print(f"Fahrenheit Menjadi\t: {fahrenheit}°F")
print(f"Kelvin Menjadi\t\t: {kelvin}°K")