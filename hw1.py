# hw1.py
# Emily Hirao + ehirao + M

######################################################################
# Place your non-autograded solutions below here!
######################################################################

"""
1a. a = 1/0
1b. f3 does not work. if both are true 2 will be put into the function 
and will return true
if both are true then b1 and b2 are both 1, 1+1>0 and will return true
2. 
f5 #return is 3 since 6^2/10 is 3.6 - truncate to 3
g3 #returns the 3 from f(x)
f4 #x was 1 from g(x) and f(4) is run
f2 #finally f is run with 2 since 5^2/10 is 2.5 - truncate to 2
5 #5 is returned since it's a global 

3. 54 #the ones digit must be one less than the tens digit
    #must be divisible by 9
4. 
def NLPD (x,y)
    x1 = math.ceil(x)
    x2 = math.floor(x)
    y1 = math.ceil(y)
    y2 = math.floor(y)
    dx = x-int(x)
    dy = y-int(y)
    d1 = math.sqrt(((x1-x)**2+(y1-y)**2))
    d2 = math.sqrt(((x2-x)**2+(y1-y)**2))
    d3 = math.sqrt(((x1-x)**2+(y2-y)**2))
    d4 = math.sqrt(((x2-x)**2+(y2-y)**2))
    return ((dx>=.5 and dy >=.5 and round(d1, 1))
    or (dx<.5 and dy>=.5 and round(d2, 1))
    or (dx>=.5 and dy<.5 and round(d3, 1))
    or (dx < .5 and dy <.5 and round (d4, 1))


"""
echo "# 15112-S15" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/ehirao14/15112-S15.git
git push -u origin master
######################################################################
# Place your autograded solutions below here
######################################################################

import math

def maximumHeartRate(age, gender):
#     You may assume that age is a positive integer and
#     gender a string and is either "male" or "female".
#     Given these values, use the formulas on this page to
#     compute and and return the maximum heart rate:
#       http://www.aqua-calc.com/calculate/maximum-heart-rate
#     Actually, one difference: here you should return the
#     nearest int value to what the formula computes.
#     Remember that you may not use conditionals this week, so you
#     may have to use some boolean arithmetic on this problem (sigh).
    return (gender == "male" and round(203.7/(1+math.e**(0.033*(age-104.3 ))))) or (gender == "female" and round(190.2/(1+math.e**(0.0453*(age-107.5)))))

def sphereVolumeFromSurfaceArea(surfaceArea):
    # Return the volume of a sphere given its surface area, which you may assume
    # is a float.  You may need to look up the formulas for the surface area
    # and volume of a sphere.
    radius = (math.sqrt(surfaceArea/(4*math.pi)))
    sphereVolume = (4.0/3*math.pi*radius**3)
    return sphereVolume

def isDivisible(x, y):
    # returns True if x and y are both integer types and x is divisible by y,
    # and False otherwise
    return (type(x)==int and type(y)==int and y!=0 and x%y==0)

def pascalsTriangleValue(row, col):
#     Given int values row and col, this function
#     returns the value in the given row and column of Pascal's Triangle
#     where the triangle starts at row 0, and each row starts at column 0.
#     If row and col are not legal values, returns False, instead of crashing.
#     Hint: math.factorial may be helpful!
    return (type(row)==int and type(col)==int and row>=0 and col>=0
    and (row>=col) and (math.factorial(row)/(math.factorial(col)*math.factorial(row-col))))

def nearestOdd(x):
#     Return the nearest odd integer to x, which may be a float.
    oddOrEven = math.floor(x)%2
    Odd = int(x+1)

    return ((x>=0 and int(oddOrEven) == 0 and
    int(x+1)) or ((x>=0 and int(oddOrEven) == 1
    and int(x)) or (x<=0 and int(math.ceil(x)%2 ==0 and type(x) == int and int(x+1))) or
    (x<=0 and int(math.ceil(x)%2) == 0 and type(x) == float and int(x-1)) or
    (x<=0 and int(math.ceil(x)%2 !=0 and int(x)))))

def rectanglesOverlap(left1, top1, width1, height1,
                       left2, top2, width2, height2):
#     A rectangle can be described by its left, top, width, and height.
#     This function takes two rectangles described this way, and
#     returns True if the rectangles overlap at all (even if just at a point),
#     and False otherwise.
    right1=left1+width1
    bottom1=top1+height1
    right2=left2+width2
    bottom2=top2+height2

    return (((left1<=left2 and left2<=right1) or (left1<=right2 and right2<=right1) 
        or (left2<=left1 and right1<=right2)or(left2>=left1 and right1>=right2)) 
        and ((top1<=top2 and top2<=bottom1) or (top1<=bottom2 and bottom2<=bottom1) 
        or (top2<=top1 and bottom1<=bottom2)or(top2>=top1 and bottom1>=bottom2)))

def cosineZerosCount(r):
#     r is a float, and this function returns the integer
#     number of zeros of cosine(x) for r radians where 0 <= x <= r.
#     You may need to Google about the shape of the graph of cosine,
#     if you don't know where its zeros are (where it crosses the x axis).
#     For example, pi/2 is one such zero.  You can also look at the
#     test function below (as you should!) to see some others!
#     (r%(math.pi/2) == 0 and r%math.pi!=0
    zero=int((r)/(math.pi/2))
    return ((r>math.pi/2 and r<math.pi and zero%2==1 and
    zero) or  (r>math.pi and zero%2==0 and int(r/math.pi)) or
    (r>math.pi and zero%2==1 and int(r/math.pi+1)) or (r<math.pi/2 and 0))

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

def almostEqual(d1, d2, epsilon=10**-3):
    return abs(d1 - d2) < epsilon

def testMaximumHeartRate():
    print "Testing maximumHeartRate()...",
    assert(maximumHeartRate(30, "male") == 188)
    assert(maximumHeartRate(30, "female") == 185)
    assert(maximumHeartRate(1, "male") == 197)
    assert(maximumHeartRate(1, "female") == 189)
    assert(maximumHeartRate(100, "male") == 109)
    assert(maximumHeartRate(100, "female") == 111)
    print "Passed!"

def testSphereVolumeFromSurfaceArea():
    print "Testing sphereVolumeFromSurfaceArea()...",
    # From http://www.aqua-calc.com/calculate/volume-sphere, with r=3, we see:
    assert(almostEqual(sphereVolumeFromSurfaceArea(452.38934),  904.77868) == True) # r=6
    assert(almostEqual(sphereVolumeFromSurfaceArea(113.09734), 113.09734) == True) # r=3
    assert(almostEqual(sphereVolumeFromSurfaceArea(452.38934),  904) == False) # r=6
    assert(almostEqual(sphereVolumeFromSurfaceArea(452.38934),  905) == False) # r=6
    assert(almostEqual(sphereVolumeFromSurfaceArea(113.09734), 113) == False) # r=3
    assert(almostEqual(sphereVolumeFromSurfaceArea(113.09734), 113.1) == False) # r=3
    print "Passed!"

def testIsDivisible():
    print "Testing isDivisible()...",
    assert(type(isDivisible(4, 2)) == bool)
    assert(isDivisible(4,2) == True)
    assert(isDivisible(2,4) == False)
    assert(isDivisible(2,2) == True)
    assert(isDivisible(2,0) == False)
    assert(isDivisible(0,2) == True)
    assert(isDivisible(3.4, 1.7) == False) # not integers
    assert(isDivisible(3.0, 2) == False) # not integers
    print "Passed!"

def testPascalsTriangleValue():
    print "Testing pascalsTriangleValue()...",
    assert(type(pascalsTriangleValue(0,0)) == int)
    assert(pascalsTriangleValue(0,0) == 1)
    assert(pascalsTriangleValue(1,0) == 1)
    assert(pascalsTriangleValue(1,1) == 1)
    assert(pascalsTriangleValue(2,0) == 1)
    assert(pascalsTriangleValue(2,1) == 2)
    assert(pascalsTriangleValue(2,2) == 1)
    assert(pascalsTriangleValue(3,0) == 1)
    assert(pascalsTriangleValue(3,1) == 3)
    assert(pascalsTriangleValue(3,2) == 3)
    assert(pascalsTriangleValue(3,3) == 1)
    assert(pascalsTriangleValue(8,3) == 56)
    assert(pascalsTriangleValue(3,3.5) == False) # 3.5 is not an int
    assert(pascalsTriangleValue(3,3.0) == False) # 3.0 is not an int
    assert(pascalsTriangleValue(3,-1) == False) # col -1 is out of range
    assert(pascalsTriangleValue(3,4) == False)  # col 4 is out of range for row 3
    assert(pascalsTriangleValue("dog", "cat") == False)  # ridiculous
    print "Passed!"

def testNearestOdd():
    print "Testing nearestOdd()...",
    assert(type(nearestOdd(3.0)) == int)
    assert(nearestOdd(0) == 1)
    assert(nearestOdd(0.75) == 1)
    assert(nearestOdd(1.0) == 1)
    assert(nearestOdd(1.9999) == 1)
    assert(nearestOdd(2.0) == 3)
    assert(nearestOdd(3) == 3)
    assert(nearestOdd(3.9999) == 3)
    assert(nearestOdd(4) == 5)
    assert(nearestOdd(-2.001) == -3)
    assert(nearestOdd(-2) == -1)
    assert(nearestOdd(-0.0001) == -1)
    print "Passed!"

def testRectanglesOverlap():
    print "Testing rectanglesOverlap()...",
    assert(type(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2)) == bool)
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2) == True)
    print "Passed!"

def testCosineZerosCount():
    print "Testing cosineZerosCount()...",
    assert(type(cosineZerosCount(0)) == int)
    assert(cosineZerosCount(0) == 0)
    assert(cosineZerosCount(math.pi/2 - 0.0001) == 0)
    assert(cosineZerosCount(math.pi/2 + 0.0001) == 1)
    assert(cosineZerosCount(3*math.pi/2 - 0.0001) == 1)
    assert(cosineZerosCount(3*math.pi/2 + 0.0001) == 2)
    assert(cosineZerosCount(5*math.pi/2 - 0.0001) == 2)
    assert(cosineZerosCount(5*math.pi/2 + 0.0001) == 3)
    assert(cosineZerosCount(-math.pi/2 - 0.0001) == 0)
    assert(cosineZerosCount(-math.pi/2 + 0.0001) == 0)
    print "passed!"

def testAll():
    testMaximumHeartRate()
    testSphereVolumeFromSurfaceArea()
    testIsDivisible()
    testPascalsTriangleValue()
    testNearestOdd()
    testRectanglesOverlap()
    testCosineZerosCount()


if __name__ == "__main__":
    testAll()