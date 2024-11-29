import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 *\
          math.cos(2*k) - 2 *\
          math.cos(3*k) -\
          math.cos(4*k)

speed(1000)  # Fastest drawing speed
bgcolor("black")
penup()  # Lift the pen to avoid drawing lines
goto(0, 0)  # Start at the center
pendown()
color("#f73487")  # Set heart color

for i in range(360):  # Adjust range for smooth drawing
    k = math.radians(i)  # Convert degrees to radians
    goto(hearta(k) * 20, heartb(k) * 20)
    for j in range(5):  # Adjust range for smooth drawing
        color("#f73487")

    goto(0,0)

done()
