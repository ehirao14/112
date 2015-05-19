# hw2.py
# Emily Hirao + ehirao + M==

######################################################################
# Place your non-autograded solutions below here!
######################################################################
#
"""
1a. and (b!=0)

1b. if b==0:
        return false
    else:


9 1 4 7 B #first prints 9, then print 1 4 7 since there are increments of 3, 9 isn't inclusive, prints B since 9/3=3 and 9%3=0
5 1 4 A #subracts 4 and gets 5. prints 1 4 since increments are 3, 5 is less than 7 and isn't inclusive, prints A since 5%3=2
1 A #subtracts 4 gets 1. Doesn't print anything from the for loop since 1 is not inclusive. prints A since 1%3=1
#exists while loop since 1-4 is negative
None

Reasoning: 3,10,3

Free Response: 
def nthFooey(n):
    counter = 0
    num=11
    while (counter<n):
        num+=1
        if (Fooey(num)==True):
            counter+=1
    return num
def Fooey(n):
    if (n%10==9):
        return True
    elif (n%10==1):
        return True
    else:
        return False
"""

######################################################################
# Place your autograded solutions below here
######################################################################


def findZeroWithBisection(function, lower, upper, error):
    y0 = function(lower)
    y1 = function(upper)
    xmid = (upper+lower)/2.0
    higherror = 0+error
    lowerror = 0-error
    if (y0 == 0):
        return lower
    elif (y1 == 0):
        return upper
    elif ((y0>0 and y1>0) or (y0<0 and y1<0)):
        return None
    print 0 #makes sure while loop starts
    n=error+1
    while (abs(n)>higherror):
        xmid = (upper+lower)/2.0
        n=function(xmid)
        if n<lowerror:
            lower = xmid
        elif n>higherror:
            upper = xmid
    return xmid 

def nthEmirp(n):
    counter = 0
    num=13
    while (counter<n):
        num+=1
        if (fasterIsPrime(num)==True and fasterIsPrime(Emirp(num))==True and palindromePrime(num)==False):
            counter+=1
    return num

def Emirp(n):
    emirp = 0
    for x in xrange(0,(findDigitplace(n)+1)):
        if (findDigitplace(n)>0):
            emirp+=(10**(findDigitplace(n))*digit(n))
            n=n/10
        else:
            emirp+=(10**(findDigitplace(n))*digit(n))
    return (emirp)
def palindromePrime(n):
    if n==Emirp(n):
        return True
    else:
        return False

def findDigitplace(n):
    counter = 0
    while (n/10>0):
        n=n/10
        counter+=1
    return counter
def digit(n):
    number = n%10
    while (n/10>0 or n%10==0):
        if (n/10>0):
            n=n/10
    return number

#fromnotes
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

def carrylessAdd(x,y):
    num = 0
    if (x==0):
        num =y
    elif (y==0):
        num=x
    elif (x>y or x==y):
        for i in xrange (0, (findDigitplace(x)+1)):
            if (y==0):
                num+=(10**i)*(digit(x)%10)
            else:
                num+=(10**i)*((digit(x)+digit(y))%10)
                x/=10
                y/=10
    elif y>x:
        for i in xrange (0, (findDigitplace(y)+1)):
            if (x==0):
                num+=(10**i)*(digit(y)%10)
            else:
                num+=10**i*((digit(x)+digit(y))%10)
                x/=10
                y/=10
    return num

# def play112(game):
#     board = makeBoard(getLeftmostDigit)
#     if (isFull(board) == False and isWin(board)== False):
#         return board+": Unfinished!"
#     if (isFull(b

def makeBoard(moves):
    num=0
    for i in xrange (0, moves):
        num+=(10**i)*8
    return num

def digitCount(n):
    return findDigitplace(abs(n))+1

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

def replaceKthDigit(n,k,d):
    if (k==0):
        return n/10*10+d
    elif (k<findDigitplace(n)):
        return (n/(10**(k+1))*10**(k+1)) + ((10**k)*d)+(n%10**k)
    else:
        return (n%10**k)+(d*10**k)


def getLeftmostDigit(n):
    return kthDigit(n,findDigitplace(n))

def clearLeftmostDigit(n):
    return n-getLeftmostDigit(n)*10**findDigitplace(n)

def makeMove(board, position, move):
    boardnumber = digitCount(board)
    if move !=1 and move != 2:
        return "move must be 1 or 2!"
    elif position>boardnumber or position<1:
        return "offboard!"
    elif (kthDigit(board, boardnumber-position)== (1 or 2)):
        return "occupied!"
    else:
        return replaceKthDigit(board,boardnumber-position, move)

def isWin(board):
    while digitCount(board)>=3:
        n=digitCount(board)
        if ((kthDigit(board, n-1)*100) + (kthDigit(board, n-2)*10) + (kthDigit(board, n-3)) == 112):
            return True
        else: board=clearLeftmostDigit(board)
    return False

def isFull(board):
    while digitCount(board)>0:
        n=digitCount(board)
        if (kthDigit(board,n-1)==8):
            return False
        elif (digitCount(board)==1):
            return True
        else:board = clearLeftmostDigit(board)
    return True


######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

