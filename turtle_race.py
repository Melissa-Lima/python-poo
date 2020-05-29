from turtle import Turtle
from random import randint

jojo = Turtle()
lala = Turtle()
joji = Turtle()
kon = Turtle()

jojo.color('red')
jojo.shape('turtle')

jojo.penup()
jojo.goto(-160, 100)
jojo.pendown()

lala.color('pink')
lala.shape('turtle')

lala.penup()
lala.goto(-160, 70)
lala.pendown()

joji.color('green')
joji.shape('turtle')

joji.penup()
joji.goto(-160, 40)
joji.pendown()

kon.color('blue')
kon.shape('turtle')

kon.penup()
kon.goto(-160, 10)
kon.pendown()

for movement in range(100):
    jojo.forward(randint(1,5))
    lala.forward(randint(1,5))
    joji.forward(randint(1,5))
    kon.forward(randint(1,5))

input("Press Enter to close")