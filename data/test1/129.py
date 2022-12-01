# Modules
import turtle
from math import sqrt


t = turtle.Turtle(visible = False)

class Boat:
    def __init__(self, length, colour):
        self.length = length
        self.height = 0.1 * sqrt(2) * length
        self.mastHeight = length * 2/3
        self.sailHeight = self.mastHeight * 0.7
        self.colour = colour
        
# Turtle manipulation functions
def f(x):
    t.forward(x)
def r(x):
    t.right(x)
def l(x):
    t.left(x)    

# Draw function
def drawBoat(size, col):
    
    # Define boat object
    boat = Boat(size, col)
    
    # Starting position
    t.color("white")
    r(180)
    f(boat.length / 2)
    r(180)
    
    # Draw hull
    t.color(boat.colour)
    f(boat.length)
    r(135)
    f(boat.height)
    r(45)
    f(0.8 * boat.length)
    r(45)
    f(boat.height)
    r(135)
    
    # Reposition
    f(boat.length / 3)
    l(90)
    
    # Draw mast + sail
    f(boat.mastHeight)
    r(90)
    f(boat.mastHeight * 0.05)
    r(45)
    f(sqrt(2) * boat.sailHeight)
    r(135)
    f(boat.sailHeight)
    r(90)
    f(boat.sailHeight)
    r(180)
    f(boat.mastHeight)
    
if __name__ == "__main__":
    # Usage: drawBoat( SIZE, COLOUR ) to spawn a boat
    drawBoat(300, "red")
    
turtle.done()
