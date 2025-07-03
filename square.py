import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.title("Square using Turtle")

# Create a turtle object
my_turtle = turtle.Turtle()
my_turtle.pensize(3)       # Set the pen thickness
my_turtle.color("blue")    # Set the color of the turtle

# Draw a square
for _ in range(4):
    my_turtle.forward(100)  # Move forward by 100 units
    my_turtle.left(90)      # Turn left by 90 degrees

# Hide the turtle after drawing
my_turtle.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
