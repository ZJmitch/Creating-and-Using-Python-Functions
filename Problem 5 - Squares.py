#Justin Mitchell
#2/23/2021

#Problem 5 produce square image

import turtle

def drawSquare(t, sz):

    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

#I know I could have referred to the function but watned to practice free drawing for game final project.

alex.forward(250)
alex.left(90)
alex.forward(250)
alex.left(90)
alex.forward(250)
alex.left(90)
alex.forward(250)

alex.up()
alex.goto(50,225)
alex.down()

alex.right(90)
alex.forward(25)
alex.left(90)
alex.forward(200)
alex.left(90)
alex.forward(200)
alex.left(90)
alex.forward(200)
alex.left(90)
alex.forward(200)

alex.up()
alex.goto(50,200)
alex.down()


alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(150)

alex.up()
alex.goto(75, 175)
alex.down()

alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(100)

alex.up()
alex.goto(100, 150)
alex.down()

alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)




wn.exitonclick()


#Program draws square picture from lab assignment
