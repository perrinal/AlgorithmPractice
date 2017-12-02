###################################################
# Implementation of the Midpoint Circle algorithm #
###################################################
#
# https://en.wikipedia.org/wiki/Midpoint_circle_algorithm
# this is a very optimised way to draw a circle on screen (when the pixel resolution is not infinite)
#
# Click anywhere on the windows to draw a circle.


from tkinter import *
import time
from time import sleep


root = Tk()
root.title = "Game"
root.resizable(0,0)
root.wm_attributes("-topmost", 1)
colours = ["#ffffff","#00ffff","#ff00ff","#ffff00","#0000ff","#ff0000","#00ff00"]
canvas = Canvas(root, width=640, height=480, bd=0, highlightthickness=0, bg="#000000")
canvas.pack()


class Circle:
    
    def __init__(self, delay=0):

        self.delay = delay
        self.colour = 0
        self.canvas = canvas
        self.WIDTH, self.HEIGHT = 640, 480
        self.CENTREX, self.CENTREY = int(self.WIDTH/2) , int(self.HEIGHT/2)

        canvas.bind("<Button-1>", self.canvas_onclick)

        self.img = PhotoImage(width=self.WIDTH, height=self.HEIGHT)
        #self.draw()
        self.img2 = canvas.create_image((self.WIDTH/2, self.HEIGHT/2), image=self.img, state="normal") 
        mainloop()

    def canvas_onclick(self, event):
        self.draw()

    def drawPoint(self,color , X,Y):
        if X > 0 and Y > 0:
            self.img.put(color, (X, Y))
    
    def draw(self):
        radius = 100
        self.colour = (self.colour + 1 ) % len(colours)
        centerX = root.winfo_pointerx() - root.winfo_rootx()
        centerY = root.winfo_pointery() - root.winfo_rooty()
        
        y = 0
        x = radius
        radiusError = 0
        
                
        while y <= x:      
            self.drawPoint(colours[self.colour], centerX + x,centerY + y)
            self.drawPoint(colours[self.colour], centerX + y,centerY + x)
            self.drawPoint(colours[self.colour], centerX - x,centerY + y)
            self.drawPoint(colours[self.colour], centerX - y,centerY + x)
            self.drawPoint(colours[self.colour], centerX + x,centerY - y)
            self.drawPoint(colours[self.colour], centerX + y,centerY - x)
            self.drawPoint(colours[self.colour], centerX - x,centerY - y)
            self.drawPoint(colours[self.colour], centerX - y,centerY - x)
            
            if radiusError <= 0:
                y = y + 1
                radiusError = radiusError + 2 * y + 1

            if radiusError > 0:
                x = x - 1
                radiusError = radiusError - 2 * x - 1
                
            sleep(self.delay)
            canvas.itemconfigure(self.img2, image=self.img)
            root.update_idletasks()
            root.update()
        
        
# The delay help to visualise how circles are drawn            
Crcl = Circle(0.001)





















