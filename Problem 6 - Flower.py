#Justin Mitchell
#2/25/2021

#Problem 6 using a polygon function to create a pattern


import turtle


wn= turtle.Screen()

alex = turtle.Turtle()
alex.color("Purple")


def drawFlower(fl):

    for i in range(8):
        for p in range(5):
            alex.right(72)
            alex.forward(100)
        alex.right(45)
    fl()

draw = drawFlower(alex)

print (draw)


#Program has defined function that draws flower. Program then prints design 
    
    
