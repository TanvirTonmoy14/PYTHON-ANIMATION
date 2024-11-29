import turtle

arms = turtle.Turtle()
arms.shape("turtle")
arms.speed(10)  # Adjust speed for clarity
arms.color("blue", "red")

# Loop to create the star
for i in range(5):  # A 5-pointed star requires 5 iterations
    arms.forward(300)  # Length of each arm
    arms.left(144)     # The angle for a star is 144 degrees

# Close the turtle graphics window when done
turtle.done()
