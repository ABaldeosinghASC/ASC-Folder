from random import *
def setup():
    size(500,500)
    stroke(0, 0, 0) 
    #RED
    fill(255,255,255) 
    rect(0,0,100,100)
    #GREEN
    fill(255,255,255)
    rect(100,0,100,100)
    #BLUE
    fill(255, 255, 255) 
    rect(200,0,100,100)
    #YELLOW
    fill(255, 255, 255)
    rect(300,0,100,100)
    #PINK
    fill(255, 255, 255)
    rect(400,0,100,100)
    #CYAN
    fill(255, 255, 255)
    rect(500,0,100,100)
    #WHITE
    fill(255, 255, 255)
    rect(600,0,100,100)
    #BLACK
    fill(255, 255, 255)
    rect(700,0,100,100)
    y = 0
    x = 0
    i = 0
    while i < 5 : # Second row
          #y + 100
          fill(255, 255, 255)
          rect(i * 100, y + 100, 100, 100)
          i = i + 1
    i = 0
    while i < 5 : #third row
          #y + 100
          fill(255, 255, 255)
          rect(i * 100, y + 200, 100, 100)
          
          i = i + 1
    i = 0
    while i < 5: 
        fill(255, 255, 255)
        rect(i * 100, y + 300, 100, 100)
        
        i = i + 1
    i = 0
    while i < 5: 
        fill(255, 255, 255)
        rect(i * 100, y + 400, 100, 100)
        i = i + 1

        

def draw():
    
    
    if mousePressed:
        fill(0, 0, 255)
        ellipse(50, 50, 99, 99)