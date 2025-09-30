#uloha 6
a=int(input("Zadaj mi cislo:"))
if a%4==0:
    print ("cislo je delitelne 4mi")
if a%7==0:
    print ("cislo je delitelne 7mimi")
if a%4!=0 and a%7!=0:
    print("cislo nieje delitelne ani 4kou ani 7mickou")
if a%4==0 and a%7==0:
    print("cisloje delitelne aj4kou ani 7mickou")
