#uloha 14
z= int(input("zadaj mi hodnotu z(spodna hranica):"))
k=int(input("zadaj mi hodnotu k(horna hranica):"))
pocet_cisel=0
for i in range (z, k+1):
    if i%8==0:
        pocet_cisel+=1
print (pocet_cisel)