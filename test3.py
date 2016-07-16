from Myro import *
init("sim") #Start simukator
forward(3,1)
backward (3,2)
turnBy(-90, "deg") #=> 
turnBy(-33, "deg") #=>
forward (3,3)
turnBy(90, "deg") 
forward(1,2)
turnBy(75, "deg")
forward(3,8)
turnBy(155, "deg")
forward(3,20)
pic=takePicture()
show(pic)