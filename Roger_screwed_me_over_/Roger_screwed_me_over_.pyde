from random import*
from time import *

def setup():
    size(500, 500)
    background(255, 255, 255)

def afunc():
    return[choice(alphabet), x, y]
    
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i","j","k","l","m","n","o","p","q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
x = 0
y = randint(0, 300)
letandpos = []  #letter and position
letandpos.append(afunc()) #make a new letter and add to our list
score = 0 # count of score


def draw():
    print(letandpos)
    background(255, 255, 255)
    global x
    global y
    global letandpos
    global alphabet
    global score
    item = 0
    textSize(30)
    text("Score", 0, 30)
    text(score, 90, 30)

    while item < len(letandpos):
        print("hello world")
        fill(255,0,0)
        text(letandpos[item][0],letandpos[item][1], letandpos[item][2])
        letandpos[item][1] = letandpos[item][1] + 2 #updating the x coordinates
        #sleep(1)
        if keyPressed:
            if key == letandpos[item][0]:
                letandpos.pop(item)
                letandpos.append(afunc()) #make a new letter and add to our list
                score += 1
            
                
        if letandpos[item][1] > 500:
           letandpos.pop(item)
    #     
           
           
                
    
       
    





    

    
 