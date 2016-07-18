def setup():
    size(800,800)
    noStroke() 
    #RED
    fill(255,0,0) 
    rect(0,0,100,100)
    #GREEN
    fill(0,255,0)
    rect(100,0,100,100)
    #BLUE
    fill(0, 0, 255) 
    rect(200,0,100,100)
    #YELLOW
    fill(255, 255, 0)
    rect(300,0,100,100)
    #PINK
    fill(255, 20, 147)
    rect(400,0,100,100)
    #CYAN
    fill(0, 255, 255)
    rect(500,0,100,100)
    #WHITE
    fill(255, 255, 255)
    rect(600,0,100,100)
    #BLACK
    fill(0, 0, 0)
    rect(700,0,100,100)
    
theSetColor = 1
def draw():
    global theSetColor   
    if mouseY < 100:
        if mouseX < 100 and mousePressed: # Red Box #My current color is now going to be red
           theSetColor = 1          
        if mouseX > 100 and mouseX < 200:
            theSetColor = 2 
    elif mouseY > 100:
        if mousePressed and theSetColor == 1: 
            fill(255, 0, 0)
            ellipse(mouseX, mouseY, 20 ,20)
        
        if mousePressed and theSetColor == 2:
            fill(0, 255, 0)
            ellipse(mouseX, mouseY, 20 ,20)

        if mousePressed and theSetColor == 3:
            fill(0, 0, 255)
            ellipse(mouseX, mouseY, 20 ,20)
       
        if mousePressed and theSetColor == 4:
            fill(255, 215, 0)
            ellipse(mouseX, mouseY, 20 ,20)
        
        if mousePressed and theSetColor == 5:
            fill(255, 20, 147)
            ellipse(mouseX, mouseY, 20 ,20)
        
        if mousePressed and theSetColor == 6:
            fill(0, 255, 255)
            ellipse(mouseX, mouseY, 20 ,20)
       
        if mousePressed and theSetColor == 7:
            fill(255, 255, 255)
            ellipse(mouseX, mouseY, 20 ,20)
       

            fill(0, 0, 0)
            ellipse(mouseX, mouseY, 20 ,20)