print("Mengkonversi Celcius")

celcius = int(input('Masukkan suhu celcius : '))

fahrenheit = (9/5 * celcius) + 32
reamur = (4/5) * celcius
kelvin = celcius + 273

print(f"\n{celcius}°C\n{"-"*20}\nDIKONVERSIKAN\n{"-"*20}")
print(f"Fahrenheit menjadi\t: {fahrenheit}°F")
print(f"Reamur menjadi\t\t: {reamur}°R")
print(f"Kelvin menjadi\t\t: {kelvin}°K")