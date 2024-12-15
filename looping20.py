nilai = int(input("Masukkan nilai perkalian : "))

print("    *", end = "")
for x in range(1, nilai + 1):
    print(f"{x:5}",end="")
print()

for x in range(1, nilai + 1):
    print(f"{x:5}",end = "")
    for y in range(1, nilai + 1):
        print(f"{x * y:5}",end="")
    print()