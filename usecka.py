from PIL import Image
A1 = int(input("zadaj mi suradnice A1:"))
A2 = int(input("zadaj mi suradnice A2:"))
B1 = int(input("zadaj mi suradnice  B1:"))
B2 = int(input("zadaj mi suradnice B2:"))

pic = Image.new("RGB",(200,200), "white")
pixels = pic.load()

if A1!=B1:
    a = (A2-B2)/(A1-B1)
    b = (A2-A1)*((A2-B2)/(A1-B1))
    if A1<B1 and A2<B2:
        if abs(A1-B1)>abs(A2-B2):
            for x in range(A1,B1+1):
            
                y = int(a*x-b)
                pixels[x,y] = (0,0,0)



    
        else:
            for y in range(A2,B2+1):
                x = int((y-b)/a)
                pixels[x,y] = (0,0,0)
    else:
        if abs(A1-B1)>abs(A2-B2):
            for x in range(B1,A1+1):
            
                y = int(a*x-b)
                pixels[x,y] = (0,0,0)



    
        else:
            for y in range(B2,A2+1):
                x = int((y-b)/a)
                pixels[x,y] = (0,0,0)
else:
    if A2 < B2:
        for y in range(A2, B2 + 1):
            pixels[A1, y] = (0, 0, 0)
    else:
        for y in range(B2, A2 + 1):
            pixels[A1, y] = (0, 0, 0)
    

pic.show()


