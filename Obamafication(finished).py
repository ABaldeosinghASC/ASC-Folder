from Myro import *
pic = makePicture("ferrari.jpg")
pixels = getPixels(pic)

obamaDarkBlue = makeColor(0,51,76)
obamaRed = makeColor(217, 26, 33)
obamaBlue = makeColor(112,150,158)
obamaYellow = makeColor(252, 227, 166)
##If a pixel's gray value is greater than 180, 
#then change that pixel's color to Obama-Yellow.  
#If the gray value is greater than 120, then the 
#pixel should be changed to Obama-Blue.  
#If the gray value is greater than 60, 
#then the pixel should be changed to Obama-Red. 
#Otherwise the pixel should be Obama-DarkBlue

for pixel in pixels:
    gray = getGray(pixel)
    if gray > 180:
        setColor(pixel,obamaYellow)
    elif gray > 120:
        setColor(pixel,obamaBlue)
    elif gray > 60: 
        setColor(pixel,obamaRed)
    else: 
        setColor(pixel,obamaDarkBlue)
show(pic)     