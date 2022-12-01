#Kirjuta programm, mis joonistab õpiku 1. peatükis tutvustatud kilpkonnaga lihtsa külgvaates laeva (võib kujutada ka muid elemente).

#Vihje. Pliiatsi ületõstmise ja allalaskmise käsud on vastavalt up() ja down().

#Programm laadi üles Moodle'isse. Selleks, et automaatkontroll su faili üles leiaks, anna talle nimi kodu1.py

from turtle import *

forward(100)
right(120)
forward(50)
right(60)
forward(50)
right(60)
forward(50)

up()
right(120)
forward(25)
left(75)
down()

forward(92)
right(75)
right(90)
a=(((92**2)-(25**2))**0.5)
forward(a)