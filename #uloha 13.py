#uloha 13
N= int(input("zadaj mi hodnotu N:"))
sucetnik=0
for i in range (1, N+1):
    if i%2==0:
        sucetnik+=i
print(sucetnik)