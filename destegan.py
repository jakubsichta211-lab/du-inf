from PIL import Image
obr = Image.open("finale.png")

def odkodovanie(picture):
    pixels = picture.load()
    bin_sprava = ""
    width, height = picture.size
    for y in range(height):
        for x in range(width):
            modra = pixels[x,y][2]
            posl_bit = bin(modra)[-1]
            temp = bin(modra)[2::]
            if len(temp)<7:
                nuly = 7-len(temp)
                temp = "0"*nuly+temp
                
            bin_sprava += temp+posl_bit
  


    sprava = ""
    for i in range(0, len(bin_sprava)):
        temp = bin_sprava[i:i+7]
        if len(temp)<7:
            break
        znak = chr(int(temp, 2))
        if znak == "#":
           break
        sprava += znak
    return sprava
print(odkodovanie(obr))
