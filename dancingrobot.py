from Myro import *
init("sim")

i = 0
while i < 3:
    motors(3, 0, 2)
    motors(0, -3, 2)
    turnBy(45, "deg")
    motors(-3, 0, 2)
    forward(3,1)
    backward(3,1)
    i = i + 1

j = 0
while j <360:
    forward(1,1)
    turnBy(1, "deg")
    j = j + 1
     