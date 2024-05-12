from turtle import Turtle,Screen
import random
import math
screen = Screen() #Creating Screen Object
screen.setup(width=800,height=600)
width = 800
screen.title('TIC TAC TOE')
# Variables
shape_count = 0
blocksize = 50
dimension = 3
lineposX = -blocksize*(dimension//2) - blocksize//2
lineposY = blocksize*(dimension//2) + blocksize//2
positionX = []
positionY = []
shape = []
winner = False
clickCount = 0

winTurtle = Turtle()
winTurtle.penup()
winTurtle.hideturtle()
winTurtle.goto(0, screen.window_height() // 2 - 20)

# Functions using
def closeScreen():
    """Close the game window"""
    screen.bye()
def printingWinner():
    global winner, clickCount, winTurtle

    clickCount += 1
    winTurtle.clear()

    if winner:
        winTurtle.write("WE HAVE A WINNER!", align="center", font=("Arial", 16, "normal"))
    elif clickCount == 10:
        winTurtle.write("IT'S A DRAW!", align="center", font=("Arial", 16, "normal"))
    else:
        current_player = "Player 1" if clickCount % 2 == 1 else "Player 2"
        winTurtle.write(f"{current_player}'s Turn", align="center", font=("Arial", 16, "normal"))
    if winner == True or clickCount == 10:
        screen.ontimer(closeScreen, 2000)
printingWinner()
def NotPrintable(index):
    global positionX , positionY, shape
    for j in range (0,dimension*dimension):
        if shape[j].xcor() == positionX[index] and shape[j].ycor() == positionY[index]:
            return True
    return False

def distanceBetween(x,x1,y1,y):
    distance = (x-x1)**2 + (y-y1)**2
    distance = math.sqrt(distance)
    return distance
def postionsStore(): # To store all the possible coordinates where a player can mark either as circle or square
    global positionX, positionY,lineposX,lineposY
    x = -blocksize*(dimension//2)
    y = blocksize*(dimension//2)
    for i in range (dimension):
        for j in range (dimension):
            positionX.append(x)
            positionY.append(y)
            print(f"postion Stored is {x,y}")
            x += blocksize
        x = -blocksize*(dimension//2)
        y -= blocksize
    
postionsStore()

def creatingShape(): # Creating objects and simply storing circles and squares alternatively
    global dimension,shape
    for i in range (0,dimension*dimension):
        shapes = Turtle()
        if (i%2==0):
            shapes.shape("circle")
            shapes.color("blue")
        else:
            shapes.shape("square")
            shapes.color("red")
        shapes.hideturtle()
        shapes.penup()
        shapes.goto(0,320)
        shapes.speed(0)
        shape.append(shapes)
creatingShape()

def onMouseClick(x,y): # To check where the mouse was clicked 
    global lineposX,lineposY, blocksize, dimension, shape_count
    for i in range (dimension*dimension): # To iterate through all the positions stored
                if(distanceBetween(x,positionX[i],y,positionY[i]) <= math.sqrt(blocksize**2//2)): # To check if the coordinates of mouse click is close by any of the stored positions
                    if not NotPrintable(i): # To check if that position doesn't already has anything printed
                        shape[shape_count].goto(positionX[i],positionY[i])
                        print(f"shape went on {positionX[i],positionY[i]}")
                        shape[shape_count].showturtle()
                        shape_count+=1
                        break
    print(f"mouse click was on {x,y}")
    checkWinner()
def rowCheck():
    global blocksize,dimension, shape

    x = -blocksize*(dimension//2)
    y = blocksize*(dimension//2)
    countCircle = 0
    countSqaure = 0

    for i in range(dimension):
        for j in range(dimension):
            for shapes in shape:
                if shapes.xcor() == x and shapes.ycor() == y:
                    if shapes.shape() == "circle":
                        countCircle += 1
                    elif shapes.shape() == "square":
                        countSqaure += 1
            x += blocksize
        if countCircle == dimension or countSqaure == dimension:
            return True
        countCircle,countSqaure = 0,0
        x = -blocksize*(dimension//2)
        y -= blocksize
    return False    
def colCheck():
    global blocksize,dimension, shape

    x = -blocksize*(dimension//2)
    y = blocksize*(dimension//2)
    countCircle = 0
    countSqaure = 0

    for i in range(dimension):
        for j in range(dimension):
            for shapes in shape:
                if shapes.xcor() == x and shapes.ycor() == y:
                    if shapes.shape() == "circle":
                        countCircle += 1
                    elif shapes.shape() == "square":
                        countSqaure += 1
            y -= blocksize
        if countCircle == dimension or countSqaure == dimension:
            return True
        countCircle,countSqaure = 0,0
        x += blocksize
        y = blocksize*(dimension//2)
    return False

def leftDiagonalCheck():
    global blocksize,dimension, shape

    x = -blocksize*(dimension//2)
    y = blocksize*(dimension//2)

    countCircle = 0
    countSquare = 0

    for i in range (dimension):
        for shapes in shape:
            if shapes.xcor() == x and shapes.ycor() == y:
                    if shapes.shape() == "circle":
                        countCircle += 1
                    elif shapes.shape() == "square":
                        countSquare += 1
        if countCircle == dimension or countSquare == dimension:
            return True
        y -= blocksize
        x += blocksize
    return False

def rightDiagonalCheck():
    global blocksize,dimension, shape

    x = blocksize*(dimension//2)
    y = blocksize*(dimension//2)

    countCircle = 0
    countSquare = 0

    for i in range (dimension):
        for shapes in shape:
            if shapes.xcor() == x and shapes.ycor() == y:
                    if shapes.shape() == "circle":
                        countCircle += 1
                    elif shapes.shape() == "square":
                        countSquare += 1
        if countCircle == dimension or countSquare == dimension:
            return True
        y -= blocksize
        x -= blocksize
    return False

def checkWinner():

    global winner,winTurtle
    if winner == False:
        winner = rowCheck()
    if winner == False:
        winner = colCheck()
    if winner == False:
        winner = leftDiagonalCheck()
    if winner == False:
        winner = rightDiagonalCheck()
    printingWinner()
if winner != True and clickCount!=10:    
    screen.onscreenclick(onMouseClick)
def draw():
    #This is the UI function of our game
    global lineposX,lineposY, blocksize, dimension, shape_count
    drawer = Turtle() #Creating drawer Object
    drawer.penup()
    drawer.hideturtle()
    drawer.speed(10)
    drawer.goto(lineposX,lineposY)
    for i in range (0,dimension): # Rows
        for j in range (0,dimension): # Columns
            drawer.pendown()
            for k in range (0,4): # Square 
                drawer.fd(blocksize)
                drawer.right(90)
            drawer.fd(blocksize)
        lineposY-=blocksize
        drawer.penup()
        drawer.goto(lineposX,lineposY)
    screen.mainloop()
draw()
