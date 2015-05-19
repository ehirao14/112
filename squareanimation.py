import stepAnimation
import math


# def staticSquareAnimation(canvas, width, height, step):
#     left = 0
#     length = 100
#     theta = step * ((2*math.pi)/8)
#     x = width/2
#     y = height/2
#     length = 100
#     dy = math.sin(theta) * length
#     dx = math.cos(theta) * length
#     canvas.create_line(x-100, y, x+100, y)

# stepAnimation.run(staticSquareAnimation)


# def wraparoundSquareAnimation(canvas, width, height, step):
#     left = step % width
#     canvas.create_rectangle(left, 0, left+20, 20, fill="blue")

# stepAnimation.run(wraparoundSquareAnimation, width=200, timerDelay=1)


# def staticSquareAnimation(canvas, width, height, step):
#     left = 0
#     canvas.create_rectangle(left, 0, left+20, 20, fill="blue")

# stepAnimation.run(staticSquareAnimation)

# def sweepingSquareAnimation(canvas, width, height, step):
#     left = step
#     canvas.create_rectangle(left, 0, left+20, 20, fill="blue")

# stepAnimation.run(sweepingSquareAnimation)

def bouncingCircleAnimation(canvas, width, height, step):
    # First do the horizontal direction
    halfPeriod = 50 # steps until we reach the right side
    step = step % (2*halfPeriod)
    if (step < halfPeriod):
        m = width/halfPeriod
        left = m*step
    else:
        m = -width/halfPeriod
        left = m*(step-halfPeriod)+width
    # Now by analogy do the vertical direction
    halfPeriod = 10 # steps until we reach the bottom side
    step = step % (2*halfPeriod)
    if (step < halfPeriod):
        m = height/halfPeriod
        top = m*step
    else:
        m = -height/halfPeriod
        top = m*(step-halfPeriod)+height
    canvas.create_oval(left, top, left+20, top+20, fill="blue")

stepAnimation.run(bouncingCircleAnimation, width=400, height=100, timerDelay=8)