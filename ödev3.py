import random
liste=list()
listef=list()
for a in range(1,16): liste.append(random.randint(1,51))
liste.sort()
print(liste)
for sayi in liste:
    for b in range(1,sayi): sayi*=b
    listef.append(sayi)
print(listef)

