from turtle import*

bgcolor("aqua") #Tausta värvimuutus
speed(0) #Kiirendab protsessi
pensize(3) #Suurendab joone suurust

def kurvvasak(): #Funktsioon sujuvalt vasakule pööramiseks
    for i in range(70):
        left(0.3)
        forward(1)
    
def kurvparem(): #Funktsioon sujuvalt paremale pööramiseks
    for i in range(70):
        right(0.3)
        forward(1)
        
def kurvvasakkiire(): #Funktsioon veidi järsemalt,aga ikka sujuvalt vasakule pööramiseks
    for i in range(35):
        left(1)
        forward(0.25)
        
def kurvparemkiire(): #Funktsioon veidi järsemalt, aga ikka sujuvalt paremale pööramiseks
    for i in range(35):
        right(1)
        forward(0.25)
    
def kurvvasakkiirekiire(): #Funktsioon veel laugemalt vasakule pööramiseks, et puri kumeralt joonistada
    for i in range(100):
        left(1)
        forward(1.25)
        
def kurvvasakaeglane(): #Samuti funktsioon laugemalt vasakule pööramiseks, et purjet joonistada
    for i in range(50):
        left(0.75)
        forward(2.25)

def aken(): #Funktsioon laevaakna joonistamiseks
    up()
    color("black")
    begin_fill()
    for i in range(90):
        right(4)
        forward(0.5)
    end_fill()
    
up() #Mere joonistamine
goto(1000, 0)
color("blue")
down()
begin_fill()
for i in range(4):
    right(90)
    forward(3000)
end_fill()
up()

up() #Laev
goto(-150,-350)
down()
color("chocolate1")
begin_fill()
forward(250)
kurvvasak()
kurvvasak()
kurvvasak()
kurvparem()
kurvparem()
forward(75)
left(175)
forward(75)
kurvvasak()
forward(75)
kurvparemkiire()
right(2)
forward(75)
for i in range(2):
    kurvvasakkiire()
    kurvvasakkiire()
    kurvparemkiire()
    kurvparemkiire()
forward(150)
kurvparemkiire()
kurvparemkiire()
kurvvasakkiire()
kurvvasakkiire()
kurvparemkiire()
kurvparemkiire()
right(20)
forward(50)
kurvvasakkiire()
kurvvasakkiire()
left(20)
forward(25)
kurvparemkiire()
kurvparemkiire()
right(20)
forward(25)
kurvvasakkiire()
kurvvasakkiire()
left(20)
forward(75)
kurvvasakkiire()
kurvvasakkiire()
left(20)
forward(87)
kurvvasak()
kurvvasak()
left(47)
forward(45)
up()
color("chocolate1")
end_fill()

goto(45,-266) #Mast
color("black")
down()
left(90)
forward(309)
right(180)
forward(35)
for i in range(3):
    left(150)
    forward(i*40+55)
    left(180)
    forward(2*(i*40+55))
    left(180)
    forward(i*40+55)
    right(150)
    forward(93)

left(135) #Puri
color("white")
kurvvasakaeglane()
kurvvasakaeglane()
right(65)
kurvvasakkiirekiire()
up()

goto(-175, -240) #Aknad
aken()
goto(-125, -240)
aken()
goto(200, -275)
aken()
for i in range(7):
    goto(150-50*i,-310)
    aken()

exitonclick() #Kiire väljumine klikivajutusega