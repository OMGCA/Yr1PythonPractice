def drawSquare(startingPoint,length):
    moveTo(startingPoint[0],startingPoint[1])
    drawLine(0,length)
    drawLine(length,0)
    drawLine(0,-length)
    drawLine(-length,0)

def modulus(n):
    # Function that returns the modulus of a number
    if n < 0:
        return 0 - n
    else:
        return n

def scaleByTwo(x_pos, y_pos):
    newX = x_pos * 2
    newy = y_pos * 2
    return newX,newy

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def drawTriangle(a,b,c):
    moveTo(a[0],a[1])
    drawLine(b[0]-a[0],b[1]-a[1])
    drawLine(c[0]-b[0],c[1]-b[1])
    drawLine(a[0]-c[0],a[1]-c[1])


def timeConverter(timeInput):

    hour = floor(timeInput/3600)
    minute = floor((timeInput - hour*3600)/60)
    second = timeInput-hour*3600-minute*60
    print(str(hour) + " hour " + str(minute) + " minute " + str(second) + " second ")

def circlePoints(angle, radius):
    x = cos(radians(angle)) * radius
    y = sin(radians(angle)) * radius
    return x,y

def drawCircle(x,y,size):
    moveTo(x,y)
    for i in range(0,360):
        drawLine(size*cos(radians(i)), -size*sin(radians(i)))
        updateCanvas()
        

from math import *
from york_graphics import *

openWindow()
drawCircle(300,400,1)
updateCanvas()
waitForMouseClick()
