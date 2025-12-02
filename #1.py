#VTAKOVINA->ludsky.py
def prekladac(zaklad: str) -> str:
    sam = "aeiouy"
    finalne = []

    for slovo in zaklad.split():
        i = 0
        dekodovane = ""

        while i < len(slovo):
            n = slovo[i]
            dekodovane += n

            if n in sam:
                # vowel → skip next 2 same vowels
                i += 3
            else:
                
                i += 2

        finalne.append(dekodovane)

    return " ".join(finalne)
print (prekladac("hieeelalaooo") )
                