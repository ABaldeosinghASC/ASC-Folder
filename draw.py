from Myro import *
init ("sim")
penDown()

def letterA():
    turnBy(60, "deg")
    forward(3,1)
    turnBy(-135, "deg")
    forward(3,1)
    backward(3,.40)
    turnBy(-115, "deg")
    forward(1,1)
    
letterA()