import random

print("PERMAINAN KERTAS GUNTING BATU")

list = ["batu", "gunting", 'kertas']
player = input("Kertas/Gunting/Batu\t: ")

enemy = random.choice(list)
print(f"Pilihan musuh\t\t: {enemy}")

if player == "kertas" and enemy == "kertas" or player == "gunting" and enemy == "gunting" or player == "batu" and enemy == "batu":
    print("Permainan draw")
elif player == "kertas" and enemy == "batu" or player == "gunting" and enemy == "kertas"or player == "batu" and enemy == "gunting":
    print("\nPermainan dimenangkan oleh kamu! :)")
elif player == "kertas" and enemy == "gunting" or player == "gunting" and enemy == "batu"or player == "batu" and enemy == "kertas":
    print("\nPerrmainan dimenangkan oleh musuh :(")