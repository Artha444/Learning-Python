print("Mengkonversi Suhu Kelvin")

kelvin = int(input('Masukkan Suhu Kelvin : '))

celcius = kelvin - 273
fahrenheit = (9/5 * kelvin) - 459.67
reamur = 4/5 * (kelvin - 273)

print(f"\n{kelvin}°K\n{"-"*20}\nDIKONVERSIKAN\n{"-"*20}")
print(f"Celcius menjadi\t\t: {celcius}°C")
print(f"Fahrenheit menjadi\t: {fahrenheit}°F")
print(f"Reamur menjadi\t\t: {reamur}°R")