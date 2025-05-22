import turtle

# Function to draw a square
def draw_square(side_length):
    turtle.forward(side_length)  # Move forward
    turtle.right(90)           # Turn 90 degrees right
    turtle.forward(side_length)
    turtle.right(90)
    turtle.forward(side_length)
    turtle.right(90)
    turtle.forward(side_length)
    turtle.right(90)

# Set up the turtle
turtle.speed(2)  # Set drawing speed (1-10, 2 is slow for visibility)

# Get side length from user
try:
    side_length = float(input("Enter the side length of the square: "))
    if side_length <= 0:
        print("Please enter a positive number.")
    else:
        draw_square(side_length)
        turtle.done()  # Keep the window open until manually closed
except ValueError:
    print("Please enter a valid number.")