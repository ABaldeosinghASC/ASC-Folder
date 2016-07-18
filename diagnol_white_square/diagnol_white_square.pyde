tacogang = 0
burritosquad = -1

def setup():
    size (1000,1000)
    background(0, 0, 255)

def draw():
    global tacogang
    global burritosquad
    background (0, 0, 255)
    fill(255, 255, 255)
    stroke(255, 255, 255)
    rect(tacogang, burritosquad, 50, 50)
    tacogang = tacogang + 1
    burritosquad = burritosquad + 1

    
    