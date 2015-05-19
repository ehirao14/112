# stepAnimation.py
# version 1.01
# David Kosbie

from Tkinter import *
import tkSimpleDialog
import sys

def run(animationFn, width=300, height=300, timerDelay=128):
    class Struct(object): pass
    data = Struct()

    def reset():
        data.canvasWidth = width
        data.canvasHeight = height
        setTimerDelay(timerDelay) # in milliseconds (set to None to turn off timer)
        data.step = -1

    def doStep():
        data.step += 1
        data.stepStringVar.set("  Step %-4d" % data.step)
        data.canvas.delete(ALL)
        animationFn(data.canvas,
                    data.canvasWidth, data.canvasHeight,
                    data.step,
                   )

    def doJump():
        step = tkSimpleDialog.askinteger("Jump", "Enter the step #:")
        if (step == None):
            return # user pressed 'cancel'
        elif (step < 0):
            print "Sorry, no negative steps allowed!"
        else:
            data.step = step-1
            data.isPaused = True
            doStep()

    def onKeyPressedWrapper(event):
        if (not data._isRunning): return
        keymap = {"g":"go", "p":"pause", "s":"step", "r":"reset", "j":"jump",
                  "+":"+faster", ">":"+faster",
                  "-":"-slower", "<":"-slower",
                  "q":"quit"}
        if (event.char in keymap): buttonPressed(keymap[event.char])

    def onTimerFiredWrapper():
        if (not data._isRunning): data.root.destroy(); return
        if (not data.isPaused):
            doStep()
        data.canvas.after(data.timerDelay, onTimerFiredWrapper)         

    def quit():
        if (not data._isRunning): return
        data._isRunning = False
        if (data.runningInIDLE):
            # in IDLE, must be sure to destroy here and now
            data.root.destroy()
        else:
            # not IDLE, then we'll destroy in the canvas.after handler
            data.root.quit()

    def setTimerDelay(timerDelay):
        data.timerDelay = timerDelay
        print "New timerDelay =", timerDelay

    def buttonPressed(label):
        if (label == "go"): data.isPaused = False
        elif (label == "pause"): data.isPaused = True
        elif (label == "step"): data.isPaused = True; doStep()
        elif (label == "reset"): reset(); data.isPaused = True; doStep()
        elif (label == "jump"): doJump()
        elif (label == "+faster"): setTimerDelay(max(1, data.timerDelay/2))
        elif (label == "-slower"): setTimerDelay(2*data.timerDelay)
        elif (label == "quit"): quit()

    def initButtonFrame():
        buttonFrame = Frame(data.root)
        def bp(label): return lambda: buttonPressed(label)
        buttonLabels = ["go", "pause", "step", "reset",
                        "jump", "+faster", "-slower"]
        for (i, label) in enumerate(buttonLabels):
            b = Button(buttonFrame, text=label, command=bp(label))
            b.grid(row=0, column=i)
        data.stepStringVar = StringVar()
        data.stepStringVar.set("  Step #")
        data.label = Label(buttonFrame, textvariable=data.stepStringVar,
                           font="Courier 14 bold")
        data.label.grid(row=0, column=len(buttonLabels))
        buttonFrame.pack(side=BOTTOM)

    def runAnimation():
        reset()
        data.isPaused = False
        data.root = Tk()
        data.root.configure(bg="gray")
        data.canvas = Canvas(data.root,
                             width=data.canvasWidth,
                             height=data.canvasHeight)
        initButtonFrame()
        data.canvas.pack()
        separator = Frame(data.root, height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, pady=2)
        data.root.wm_title(animationFn.__name__)
        data.root.protocol("WM_DELETE_WINDOW", lambda: quit())
        data._isRunning = True
        data.runningInIDLE =  ("idlelib" in sys.modules)
        #data.root.bind("<Button-1>", lambda event: onMousePressedWrapper(event))
        data.root.bind("<Key>", lambda event: onKeyPressedWrapper(event))
        onTimerFiredWrapper()
        data.root.mainloop()

    runAnimation()

"""
import stepAnimation

def sweepingBallAnimation(canvas, width, height, step):
    canvas.create_rectangle(0, 0, 10, 10, fill="green")
    canvas.create_rectangle(width-10, height-10, width, height, fill="red")
    (cx, cy, r) = ((10*step) % width, height/2, 20)
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="cyan")

stepAnimation.run(sweepingBallAnimation, width=75, height=75, timerDelay=50)

# or just:

stepAnimation.run(sweepingBallAnimation)
"""

