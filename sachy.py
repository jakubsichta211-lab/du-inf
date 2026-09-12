from PIL import Image, ImageDraw
import os
chessboard = []
#
#
#
counter = 0
def create_board ():
    global chessboard
    #chessboard = [row] * 8  # mega pruser takto to nikdy nerob !!!!!
    for i in range (8):
        row = [0] * 8
        chessboard.append(row)
#
#
#





def check_it (x, y):
    for i in range (0, 8):
        if chessboard[y][i] == 1:
            return False
        if chessboard[i][x] == 1:
            return False
    for i in range(0,8):    #y
        for o in range(0,8):    #x
            if i+o == x+y:
                if chessboard[i][o] == 1:
                    return False
            if i-o == y-x:
                if chessboard[i][o] == 1:
                    return False
    return True
#
def createImage():
    global counter
    size = 80
    boardsize = 8*size
    img = Image.new("RGB", (boardsize, boardsize),"white")
    draw=ImageDraw.Draw(img)
    for y in range(8):
        for x in range(8):
            if (x + y) % 2 == 0:
                color = "black"
            else:
                color = "white"
            draw.rectangle([x * size, y * size,(x + 1) * size,(y + 1) * size],fill=color)
    for y in range(8):
        for x in range(8):
            if chessboard[y][x] == 1:
                draw.ellipse(
                    [x * size + 10, y * size + 10,
                     (x + 1) * size - 10, (y + 1) * size - 10],
                    fill="red"
                )
    os.makedirs("solutions.sichta", exist_ok=True)        
    img.save(f"solutions.sichta/solution_{counter}.png")

#
def queens(n):
    global chessboard
    global counter
    if n==8:
        counter+=1
        print (chessboard)
        createImage()
        print("---------------------------------------------")
        print(counter)
    else :
        for i in range(0,8):
            if check_it(i,n):
                chessboard[n][i]=1
                queens(n+1)
                chessboard[n][i]=0

create_board()
#
queens(0)

