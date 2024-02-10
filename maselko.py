import random
znaczki = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
dlugi = int(input("Podaj długość hasła: "))
gen = ""
for _ in range(dlugi):
    gen += random.choice(znaczki)
print("Wygenerowane hasło:" , gen)
