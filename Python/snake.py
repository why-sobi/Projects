from turtle import Turtle, Screen
import random
import math
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
# variables

diagonal = screen.window_height() // screen.window_width()
new_snake_size = 3
old_snake_size = new_snake_size
num_of_food = 2
foodX = []
foodY = []
direction = ""
score = 0
circleRadius = 10
leastDistance = 2*circleRadius + circleRadius

scoreShow = Turtle()
scoreShow.hideturtle()
scoreShow.penup()
scoreShow.color("white")
scoreShow.goto(-screen.window_width()/2, screen.window_height()//2)

head = Turtle()

tail = []

food = []

boundaries = Turtle()
boundaries.shape("square")
boundaries.color("white")
boundaries.penup()
boundaries.shapesize(stretch_len=50)
angle = 90
for i in range(0,4):

    if i == 0:
        boundaries.goto(0,screen.window_height()//2)
    elif i == 1:
        boundaries.goto(screen.window_width()//2,0)
    elif i == 2:
        boundaries.goto(0,-screen.window_height()//2)
    elif i == 3:
        boundaries.goto(-screen.window_width()//2,0)
    boundaries.stamp()
    boundaries.setheading(angle)
    angle -= 90
boundaries.hideturtle()
# Functions


def initialize():
    global head,direction,score,tail,food,num_of_food,new_snake_size,old_snake_size
    new_snake_size = 3
    old_snake_size = new_snake_size
    num_of_food = 2
    direction = ""
    score = 0

    # head

    head.penup()
    head.shape("square")
    head.color("white")
    head.goto(0, 0)
    head.speed(0)

    # tail

    for turtle in tail:
        turtle.clear()
        turtle.hideturtle()

    tail.clear()

    for i in range(new_snake_size):
        segment = Turtle()
        segment.penup()
        segment.shape("square")
        segment.color("grey")
        tail.append(segment)

    
    # food
    
    for foods in food:
        foods.clear()
        foods.hideturtle()

    food.clear()

    for i in range(num_of_food):
        eat = Turtle()
        eat.penup()
        eat.shape("circle")
        eat.color("red")
        food.append(eat)
    
    foodUpdate()
    scoreUpdate()
    direction = "Right"


def up():
    global direction
    if direction != "Down":
        direction = "Up"


def down():
    global direction
    if direction != "Up":
        direction = "Down"


def right():
    global direction
    if direction != "Left":
        direction = "Right"


def left():
    global direction
    if direction != "Right":
        direction = "Left"


screen.listen()
screen.onkey(up, "Up")
screen.onkey(right, "Right")
screen.onkey(left, "Left")
screen.onkey(down, "Down")


def movement():
    global direction,head
    x = head.xcor()
    y = head.ycor()

    if direction == "Up":
        head.sety(y + 10)

    elif direction == "Down":
        head.sety(y - 10)

    elif direction == "Left":
        head.setx(x - 10)

    elif direction == "Right":
        head.setx(x + 10)


def update():
    screen.update()

def tailUpdate():
    global tail,head,old_snake_size,new_snake_size
    
    if old_snake_size < new_snake_size:
        # Make a new segment for the snake's tail
        segment = Turtle()
        segment.penup()
        segment.shape("square")
        segment.color("grey")
        tail.append(segment)
        old_snake_size += 1

    tail[0].goto(head.xcor(),head.ycor())

    for i in range(new_snake_size - 1, 0, -1):
        tail[i].goto(tail[i - 1].xcor(),tail[i - 1].ycor())

def foodUpdate():
    food1()
    food2()

def food1():
    global food,diagonal,leastDistance
    while True:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        if abs(x - food[1].xcor()) >= leastDistance and abs(y - food[1].ycor()) >= leastDistance and abs((y - food[1].ycor())//(x - food[1].xcor())) != diagonal:
            break
    food[0].hideturtle()
    food[0].goto(x,y)
    food[0].showturtle()

def food2():
    global food,diagonal,leastDistance
    while True:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        if abs(x - food[0].xcor()) >= leastDistance and abs(y - food[0].ycor()) >= leastDistance and abs((y - food[0].ycor())//(x - food[0].xcor())) != diagonal:
            break
    food[1].hideturtle()
    food[1].goto(x,y)
    food[1].showturtle()

def scoreUpdate():
    global scoreShow,score
    toShow = "Score: "
    toShow+=str(score)
    scoreShow.clear()
    scoreShow.write(toShow, align="center", font=("Arial",  16, "normal"))
    
    
def Checks():
    global head, food,new_snake_size,score
    if head.distance(food[0]) < 20:
        food1()
        new_snake_size += 1
        score += 1
        scoreUpdate()
    elif head.distance(food[1]) < 20:
        food2()
        new_snake_size += 1
        score += 1
        scoreUpdate()
    if abs(head.xcor()) > screen.window_width()//2 or abs(head.ycor()) > screen.window_height()//2:
        initialize()
def main():
    initialize()
    while True:
        movement()
        update()
        tailUpdate()
        Checks()
        time.sleep(1 / 100)

main()
screen.exitonclick()
