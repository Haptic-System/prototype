
import communication_serie as cali_arduino
import turtle
import os
import time
import random
# import winsound
from ast import literal_eval



wn = turtle.Screen()
wn.title("Haptic System Test")
wn.bgcolor("light blue")
width = 800
height = 600
wn.setup(width=width, height=height)
wn.tracer(0)


# sphere
sphere = turtle.Turtle()
sphere.speed(0)
sphere.shape("square")
sphere.color("blue")
sphere.penup()
sphere.goto(0, 0)
sphere.pendown()


# sphere
coin = turtle.Turtle()
coin.speed(0)
coin.shape("circle")
coin.color("orange")
coin.penup()
coin.goto(200, 0)


# Pen to write title
pen = turtle.Turtle()
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Haptic System Game Test", align="center", font=("Courier", 24, "normal"))

def sphere_movement(valx, valy, valz, relative=True):
    x = sphere.xcor()
    y = sphere.ycor()
    sphere.pencolor((valz, (1-valz),0.5))
    sphere.color((valz, (1-valz),0.5))
    if relative:
        x += (valx-.5)*width
        y += (valy-.5)*height
    else:
        x = (valx-.5)*width
        y = (valy-.5)*height
    sphere.goto(x,y)



def get_mesure(nb_val = 1, call = "none"):
    if call == "first":
        time.sleep(2.6)
    val = cali_arduino.mesure(nb_val)
    while len(val) > nb_val:
        val.pop(0)
        print("voici val modifié:", val)
    if not val:
        val = 0
    else:
        val = val[0] #car val est une liste contenant 1 élément
    return val

def close_arduino():
    cali_arduino.end()


# Main game loop
wn.update()
cali_arduino.start()
valx = 0 ##get_mesure(call = "first")
valy = 0
valz=0



wn.listen()
wn.onkeypress(close_arduino, "q")

while True:
    wn.update()

    measure = cali_arduino.mesure()
    if len(measure)>0:
        #print(measure)
        valx= measure[-1][0]
        valy= measure[-1][1]
        valz= measure[-1][2]
    #print(valz)


    sphere_movement(valx,valy,valz, relative=False)

    #gérer les collisions
    if sphere.distance(coin) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        coin.goto(x, y)
        # winsound.Beep(800, 75)



    #time.sleep(0.5)
