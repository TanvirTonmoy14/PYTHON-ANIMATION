import turtle

arms = turtle.Turtle()
arms.speed(100)
arms.fd(-150)

arms.color("red","blue")

arms.begin_fill()

for i in range (90):
     arms.forward(300)
     arms.left(170)
arms.end_fill()

turtle.mainloop()
