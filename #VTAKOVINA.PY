def prekladac_opacny(zaklad: str)->str:
    import random
    sam="aeiouy"
    finalne_slovo=[]    
    for slovo in zaklad.split():
                i=0
                zakodovane=""
                for i in slovo:
                        if i in sam:
                                zakodovane+=i+i*2
                        else:
                                zakodovane+=i+ random.choice(sam)
                finalne_slovo.append(zakodovane)
        
    return" ".join (finalne_slovo)
print (prekladac_opacny("hello"))