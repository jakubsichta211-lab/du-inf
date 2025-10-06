#uloha 5
N= int(input("zadaj mi hodnotu N(spodna hranica):"))
X=int(input("zadaj mi hodnotu X(horna hranica):"))
for i in range(N, X+1):
    odmocnina=i**0.5
    print(i,round(odmocnina, 2))