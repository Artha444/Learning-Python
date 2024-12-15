print("Mengkonversi Suhu Fahrenheit")

fahrenheit = int(input('Masukkan Suhu Fahrenheit : '))

celcius = 5/9 * (fahrenheit - 32)
reamur = 4/9 * (fahrenheit - 32)
kelvin = 5/9 * (fahrenheit + 459.67) 

print(f"\n{fahrenheit}°F\n{"-"*20}\nDIKONVERSIKAN\n{"-"*20}")
print(f"Celcius Menjadi\t: {celcius}°C")
print(f"Reamur Menjadi\t: {reamur}°R")
print(f"Kelvin Menjadi\t: {kelvin}°K")