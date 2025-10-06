#uloha 9
z= int(input("zadaj mi hodnotu z(spodna hranica):"))
k=int(input("zadaj mi hodnotu k(horna hranica):"))
for i in range (z,k+1):
    if i%2!=0:
        print(i)