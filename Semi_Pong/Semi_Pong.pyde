from time import *

from random import *
xPos = randint(0,690)
yPos = randint(0,690)
xSpeed = 5 
ySpeed = 5

def setup():
    size(700, 700)
    background(255, 255, 255)
def draw():
    global xPos
    
    global yPos
    
    global xSpeed
    
    global ySpeed
    

    xPos = xPos + xSpeed
    yPos = yPos + ySpeed
   
    fill(255, 0, 0)
    background(255, 255, 255)    
    ellipse(xPos, yPos, 20, 20)
    

    if xPos >= 690:
       xSpeed = xSpeed * -1

    if yPos >= 690:
        ySpeed = ySpeed * - 1 
       
    if xPos <= 10:
       xSpeed = xSpeed * -1

    if yPos <= 10:
        ySpeed = ySpeed * - 1 
       
    

    
    
    
    
   