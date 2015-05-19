# hw3.py
# Emily Hirao + ehirao + M==

######################################################################
# Place your non-autograded solutions below here!
######################################################################
#
"""
1.
z 9
z 6
8 7 z 3
5 None

2a. should be 4 circles instead of 5
2b.creates too many grey squares
2c. Nothing wrong

3.import stepAnimation

def dotAt2(canvas, x0, y0, x1, y1, hour):
    width = (x1 - x0)
    height = (y1 - y0)
    r = min(width, height)/2
    cx = (x0 + x1)/2
    cy = (y0 + y1)/2
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline="black", width=2)
    hourAngle = math.pi/2 - 2*math.pi*hour/12
    hourRadius = r*1/2
    hourX = int(round(cx + hourRadius * math.cos(hourAngle)))
    hourY = int(round(cy - hourRadius * math.sin(hourAngle)))
    canvas.create_line(hourX-1, hourY-1, hourX, hourY, fill="black", width=1)
stepAnimation.run(dotAt2, 25, 25, 175, 150, 2) 


4. f1 returns 1 with an input 1 instead of 0 since it keeps going in the while 
loop when it should be x>1
f5 returns 1 with an input of 1 instead of 0 
"""

######################################################################
# Place your autograded solutions below here
######################################################################

import math

import stepAnimation
from Tkinter import*


#from hw2
def findDigitplace(n):
    counter = 0
    while (n/10>0):
        n=n/10
        counter+=1
    return counter

#from hw2
def kthDigit(n,k):
    num = abs(n)
    kth=0
    if (k<=findDigitplace(num)):
        for i in xrange(0, k+1):
            kth = num%10
            num/=10
    else:
        kth = 0
    return kth
#from hw2
def getLeftmostDigit(n):
    return kthDigit(n,findDigitplace(n))
#from hw2
def clearLeftmostDigit(n):
    return n-getLeftmostDigit(n)*10**findDigitplace(n)
#from notes
def fasterIsPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = int(round(n**0.5))
    for factor in xrange(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

def isAlmostPalindromic(n):
    counter = 0
    originalNumber=n
    for x in xrange(0, findDigitplace(originalNumber)):
        if kthDigit(n, 0) != getLeftmostDigit(n): #adds one to counter if first
            counter+=1 #and last digit aren't same
        n=clearLeftmostDigit(n)/10 #clears the highest digit value and ones digit
    if counter == 1: #if the counter is 1 then only 1 digit that's not same
        return True
    else: return False

def nthNearlyPalindromicPrime(n):
    counter = 0
    NPP=13 #start at 13 so that if counter = 0 the answer is 13
    while (counter<n):
        NPP+=1
        if fasterIsPrime(NPP) == True and isAlmostPalindromic(NPP)==True:
            counter+=1
    return NPP


def Carol(num):
    return (((2**num)-1)**2-2) 

def nthCarolPrime(k):
    counter=0
    CarolNum=3
    if k == 0: num =7
    while (counter<k):
        num = Carol(CarolNum)
        checkernum=fasterIsPrime(num)
        CarolNum+=1 #checks next carolnum instead of checking each number
        if checkernum == True:
            counter+=1 
    return num

def isKaprekarNumber(num):
    if (num == 1): return True
    nsquared = num**2
    count = 1 # count tells us what exponent to use
    right = nsquared%10
    left = nsquared/10
    while (left!=0):
        if (right != 0) and (left+right == num):
            return True
        digit = left%10
        right = right+((10**count)*digit)
        left = left/10
        count += 1
    return False

def nearestKaprekarNumber(n):
    offset = n - int(n)
    upper = int(n)
    lower = int(n)
    while (not isKaprekarNumber(upper)) and (not isKaprekarNumber(lower)):
        upper+=1
        lower-=1
    if isKaprekarNumber(lower):
        if (offset > 0.5):
            upper += 1
        upperDisp = upper - n
        lowerDisp = n - lower
        if (isKaprekarNumber(upper) and (upperDisp < lowerDisp)):
            return upper
        return lower
    return upper



def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def loadingAnimation(canvas, width, height, step):
    radiusdivisor = 3
    r = min(width, height)/radiusdivisor
    cx = (width)/2
    cy = (height)/2
    positions = 14 #number of places that the circles will iterate through
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline="grey", fill="grey") #creates large circle with starting coordinates in center of page
    canvas.create_text(cx, cy, text="Loading...", font="Helvetica 26 bold")
    numCircles=8
    for position in xrange (numCircles): #creates 8 circles 
        circleColor=position
        position -= (step%positions) #creates new circles that rotate clockwise
        circleAngle = math.pi/2 - 2*math.pi*position/14 #chooses place on large circle that small circle will occupy
        startX = (cx-r * math.cos(circleAngle)) #creates new starting coordinates as the small circles move
        startY = (cy-r * math.sin(circleAngle))
        white=255
        RGB=float(white)/(numCircles-1) #makes a couple of shades of gray. oh and white and black
        changeColor=circleColor*RGB #changes color of the circles so that the leading circle is constantly black while the other have less color
        fillColor = rgbString(changeColor, changeColor, changeColor)
        canvas.create_oval(startX-r/(radiusdivisor*2), startY-r/(radiusdivisor*2), startX+r/(radiusdivisor*2), startY+r/(radiusdivisor*2), 
            outline="black", fill=fillColor)

stepAnimation.run(loadingAnimation, width = 700, height = 700)

def makeBoardH(canvas, width, height, step):
    xmargin = 10
    ymargin = 20
    endxpoint = width-xmargin
    endypoint = height-ymargin
    x0 = xmargin
    y0 = ymargin
    x1 = x0+endxpoint/5
    y1 = y0+endypoint/10
    for yposition in xrange(0,10):
        for xposition in xrange(0,5):
            if (xposition+yposition)%2 == 0:
                canvas.create_rectangle(x0, y0, x1, y1, fill="lightblue", width=2)
            else: canvas.create_rectangle(x0, y0, x1, y1, fill="pink", width=2)
            x0=x1
            x1=x0+endxpoint/5
        x0 = xmargin
        x1=x0+endxpoint/5
        y0=y1
        y1=y0+endypoint/10

def makeBoardV(canvas, width, height, step):
    xmargin = 10
    ymargin = 20
    endxpoint = width-xmargin
    endypoint = height-ymargin
    x0=xmargin
    y0=ymargin
    x1=x0+endxpoint/10
    y1=y0+endypoint/5
    for yposition in xrange(0,5):
        for xposition in xrange(0,10):
            if (xposition+yposition)%2 == 0:
                canvas.create_rectangle(x0, y0, x1, y1, fill="lightblue", width=2)
            else: canvas.create_rectangle(x0, y0, x1, y1, fill="pink", width=2)
            x0=x1
            x1=x0+endxpoint/10
        x0 = xmargin
        x1=x0+endxpoint/10
        y0=y1
        y1=y0+endypoint/5

def highlightH(canvas, width, height, step): #creates red/block animation for horizontal board
    xmargin = 10
    ymargin = 20
    endxpoint = width-xmargin
    endypoint = height-ymargin
    rectanglewidth = endxpoint/5
    rectangleheight = endypoint/10
    step%=50
    y1=0
    x1=0
    x0=xmargin
    y0=ymargin
    makeBoardH(canvas, width, height, step)

    if step%2==0:
        fillcolor = "blue"
    else: fillcolor = "red"

    if y1<=endypoint:
        y0=ymargin+(step/5*rectangleheight)
        y1=y0+rectangleheight
        if x1<=endxpoint:
            x0 = xmargin+(step%5*rectanglewidth)
            x1=x0+rectanglewidth
            canvas.create_rectangle(x0, y0, x1, y1, fill=fillcolor, width=2)
            canvas.create_text(width/2, endypoint/2, text="10 by 5", font="Helvetica 100 bold", fill="darkred")

def highlightV(canvas, width, height, step): #makes the red/blue block on the vertical board
    xmargin = 10
    ymargin = 20
    step%=50
    endxpoint = width-xmargin
    endypoint = height-ymargin
    rectanglewidth = endxpoint/10
    rectangleheight = endypoint/5
    x0=xmargin
    y0=ymargin
    y1=0
    x1=0
    makeBoardV(canvas, width, height, step)
    if step%2==0:
        fillcolor = "blue"
    else: fillcolor = "red"
    if y1<=endypoint: #checks if the rectangle has reached the end of the y axis of the board
        y0=ymargin+(step/10*rectangleheight) 
        y1=y0+rectangleheight
        if x1<=endxpoint:
            x0 = xmargin+(step%10*rectanglewidth) #constantly changes the x0 and x1 of the rectangle
            x1=x0+rectanglewidth
            canvas.create_rectangle(x0, y0, x1, y1, fill=fillcolor, width=2)
            canvas.create_text(width/2, endypoint/2, text="5 by 10", font="Helvetica 100 bold", fill="darkred")

def alternatingGridAnimation(canvas, width, height, step):
    if step/50%2==0:
        highlightH(canvas, width, height, step)
    else: highlightV(canvas, width, height, step)
stepAnimation.run(alternatingGridAnimation, width = 500, height = 500)


def makeShape(canvas, vertices, centerx, centery, color, radius, step):
        angle = 2*math.pi/vertices
        if vertices%2==0:
            movingangle = (step%18*(math.pi/18))
        elif vertices%2==1:
            movingangle = (step%18*-(math.pi/18))
        for vertex in xrange (vertices):
            x0=centerx+radius*math.cos(angle*vertex + movingangle)
            y0=centery+radius*math.sin(angle*vertex + movingangle)
            for vertexline in xrange(vertices):
                x1=centerx+radius*math.cos(angle*vertexline + movingangle)
                y1=centery+radius*math.sin(angle*vertexline + movingangle)
                canvas.create_line(x0, y0, x1, y1, fill=color, width=2)

def fancyWheelGrid(canvas, width, height, step):
    rownum, columnnum = 5, 5
    margin = 3
    widthstep = width/rownum
    centerx = width/(rownum*2)
    heightstep = height/columnnum
    centery = height/(columnnum*2)
    radius = centery
    fillcolor = "green"
    for column in xrange (columnnum):
        if column!=0:
            centery = centery+heightstep
            centerx = width/(rownum*2)
        for row in xrange (rownum):
            if(row != 0):
                centerx = centerx+widthstep
            fillcolor = rgbString((255/(columnnum-1))*(column), 255-(255/(rownum-1)*(row)), 0) #adds red as columns increases, subtracts green as rows increase
            makeShape(canvas, row+column+4, centerx, centery+margin, fillcolor, radius, step)

stepAnimation.run(fancyWheelGrid, width=800, height=600, timerDelay=128)

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################


def testNthNearlyPalindromicPrime():
    print "Testing nthNearlyPalindromicPrime()...",
    assert(nthNearlyPalindromicPrime(0) == 13)
    assert(nthNearlyPalindromicPrime(5) == 31)
    assert(nthNearlyPalindromicPrime(10)==53)
    assert(nthNearlyPalindromicPrime(195)==1999)
    print "passed!"

def testNthCarolPrime():
    print "Testing NthCarolPrime()...",
    assert(nthCarolPrime(0)==7)
    assert(nthCarolPrime(1)==47)
    assert(nthCarolPrime(2)==223)
    assert(nthCarolPrime(3)==3967)
    print "passed!"

def testNearestKaprekarNumber():
    print "Testing nearestKaprekarNumber()...",
    assert(nearestKaprekarNumber(26.99999) == 9) # should go to 9
    assert(nearestKaprekarNumber(27.0)==9) # tie, should go to 9
    assert(nearestKaprekarNumber(27.00001)==45) # should go to 45
    assert(nearestKaprekarNumber(50.00001)==55) # should go to 55
    assert(nearestKaprekarNumber(2475.499999)==2223) # should go to 2223
    assert(nearestKaprekarNumber(2475.50)==2223) # tie should go to 2223
    assert(nearestKaprekarNumber(2475.50001)==2728) # should go to 2728
    print "passed!"

def testAll():
    testNthNearlyPalindromicPrime()
    testNthCarolPrime()
    testNearestKaprekarNumber()



if __name__ == "__main__":
    testAll()




