from turtle import *

def ship():
    color('black', 'black')
    begin_fill()
    forward(100)
    left(50)
    forward(50)
    left(130)
    forward(5)
    left(30)
    forward(30)
    right(30)
    forward(200)
    right(30)
    forward(30)
    left(30)
    forward(5)
    left(130)
    forward(50)
    left(50)
    forward(100)
    end_fill()
    
    
    left(90)
    forward(6)
    pensize(10)
    forward(200)
    pensize(1)
    
    right(120)
    forward(40)
    right(120)
    forward(40)
    left(60)
    
    done()
ship()