from random import random, seed
seed(0)
n_osob = int((random()*10_000))%10_000
with open("relacje.txt","w") as new:
    for osoba in range(n_osob):
        n_relacji = int((random() * 10)) % 10 + 1
        relacje = set()
        for _ in range(n_relacji):
            sila_relacji = random().__round__(4)
            z_kim_relacja = 0
            while z_kim_relacja in relacje:
                z_kim_relacja = int((random() * 10_000)) % 10_000
            relacje.add(z_kim_relacja)
            new.write(f'{osoba},{z_kim_relacja},{sila_relacji}')
            new.write("\n")

