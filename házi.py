import math
import random 

#14
szoveg = input("Írj egy szót:")

if szoveg:
    vege = ""
    for betu in szoveg:
        vege = betu
    print(vege)


    #15
    
    szoveg2 = input("Írj egy szót:")

elso =""
vege2 = ""
talalt = False

if szoveg2:
     elso == vege2
for  egyenlo in szoveg2:
    if not talalt:
        elso = egyenlo
        talalt = True
    vege2 = egyenlo

if vege2 == elso:
    print("egyenlőek")
else:
     print("nem egyenlőek")

    #16

szoveg3 = input("Adj meg egy szöveget: ")
masodik = ""

szam = 0
for mb in szoveg3:
    if szam % 2 == 0:
        masodik += mb
    szam += 1

print("Minden második betű:", masodik)