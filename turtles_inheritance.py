#excersise when we create 2 inherited classes from main Turtle. Each has defined function to turn in predefined direction.
#after we create 20 turtles and list them
#we check the turtles in list and assign pen colors
#let all turtles draw square, each with assigned color and turning in predefined direction

from turtle import Turtle
from random import randrange as rr

class Turtle1(Turtle):  #creating inherited class from Turtle and defining function to turn it in predefined direction.
    def otoc(self, uhol):
        self.lt(uhol)

class Turtle2(Turtle):  #creating inherited class from Turtle and defining function to turn it in predefined direction
    def otoc(self, uhol):
        self.rt(uhol)

zoz = []    #list of created turtles

for i in range(20): #creating 20 turtles, if o=0 Turtle1 is created, if o=1 Turtle2 is created
    o = rr(0, 2)
    if o == 0:
        t1 = Turtle1()
        t1.seth(0)
        t1.pu()
        t1.setpos(-200 + i * 20, 0)
        t1.pd()
        zoz.append(t1)  #adding turtle into list
    else:
        t2 = Turtle2()
        t2.seth(0)
        t2.pu()
        t2.setpos(-200 + i * 20, 0)
        t2.pd()
        zoz.append(t2)  #adding turtle into list

for t in zoz:   #checking the list of turtles one by one. Changing pen color based on turtle instance
    if isinstance(t, Turtle1):
        t.pencolor('red')
    elif isinstance(t, Turtle2):
        t.pencolor('blue')

for i in range(4):  #moving turtles one after another to draw square
    for t in zoz:
        t.fd(20)
        t.otoc(90)
