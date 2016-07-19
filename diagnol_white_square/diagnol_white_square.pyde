from random import *
from math import *

def setup():
    size (1000,1000)
    background(255, 255, 255)

def draw():
    
    ellipse(mouseX, mouseY, 50, 50)
    fill(randint(0, 255),randint(0, 255),randint(0, 255)) 
    noStroke()
    for i in range(10):
        x = randrange(0,25)
        
        ellipse(mouseX + randint(-50,50), mouseY + randint(-50,50), x, x)
        fill(randint(0, 255),randint(0, 255),randint(0, 255))
    
    




    