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

        
    
          
         
         
          
    
     


theSetColor = 1

def draw():
    global theSetColor   
    
    if mouseY < 100:
        if mouseX < 100 and mousePressed: # Red Box #My current color is now going to be red
           ran          
    
    if mouseY < 100:    
        if mouseX > 100 and mousePressed < 200:
            theSetColor = 2 
    
    if mouseY < 100:
        if mouseX > 200 and mousePressed < 300:
            theSetColor = 4
    
    if mouseY < 100:
        if mouseX > 300 and mousePressed < 400:
            theSetColor = 3
    
    if mouseY < 100:
        if mouseX > 400 and mousePressed < 500:
            theSetColor = 53
    
    if mouseY < 100:
        if mouseX > 500 and mousePressed < 600:
            theSetColor = 6
    
    if mouseY < 100:
        if mouseX > 600 and mousePressed < 700:
            theSetColor = 15
    if mouseY < 100:
        if mouseX > 700 and mousePressed < 800:
            theSetColor = 0

    elif mouseY > 100:
        if mousePressed and theSetColor == 1: 
            fill(255, 0, 0)
            ellipse(mouseX, mouseY, 20 ,20)
        
        if mousePressed and theSetColor == 2:
            fill(0, 255, 0)
            ellipse(mouseX, mouseY, 20 ,20)
            
        if mousePressed and theSetColor == 4:
           fill(0, 0, 255)
           ellipse(mouseX, mouseY, 20, 20)
    
        if mousePressed and theSetColor == 3:
           fill(255, 215, 0,)
           ellipse(mouseX, mouseY, 20, 20)
           
        if mousePressed and theSetColor == 53:
           fill(255, 20, 147)
           ellipse(mouseX, mouseY, 20, 20)
           
        if mousePressed and theSetColor == 6:
           fill(0, 255, 255)
           ellipse(mouseX, mouseY, 20, 20)
        
        if mousePressed and theSetColor == 15:
           fill(255, 255, 255)
           ellipse(mouseX, mouseY, 20, 20,)
           
        if mousePressed and theSetColor == 0:
           fill(0, 0, 0)
           ellipse(mouseX, mouseY, 20, 20,)
       
           