#inspiratsioon:
#https://www.google.com/imgres?imgurl=https%3A%2F%2Fpreviews.123rf.com%2Fimages%2Fjemastock%2Fjemastock1906%2Fjemastock190615006%2F124404558-pirate-ship-boat-side-view-isolated-cartoon-vector-illustration-graphic-design.jpg&imgrefurl=https%3A%2F%2Fwww.123rf.com%2Fphoto_124404558_stock-vector-pirate-ship-boat-side-view-isolated-cartoon-vector-illustration-graphic-design.html&tbnid=tV8r0K3RSlh4BM&vet=12ahUKEwjM-ZXTst7yAhWMsCoKHXnYDL8QMygIegUIARDVAQ..i&docid=mBnbTQ80TXUAFM&w=1300&h=1300&q=boat%20side%20view&hl=en-US&ved=2ahUKEwjM-ZXTst7yAhWMsCoKHXnYDL8QMygIegUIARDVAQ
from turtle import*
"""
forward()
left()
right()
up()
down()
"""

def aknad(n):
    # n on akende arv
    if n==0:
        return None
    else:
        a =0
        while a < 4:
            left(90)
            forward(50)
            a = a + 1
        up()
        forward(100)
        down()
        return aknad(n-1)
        
#aknad(4)   
    
exitonclick()
