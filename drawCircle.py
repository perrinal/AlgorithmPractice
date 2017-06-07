from tkinter import *
import time

class DrawCircle:
    def __init__(self):
        pass 
        
    
##    def run(self):
##        
##        root = Tk()
##
##        self.entries = []
##        row = Frame(root)
##
##        label = Label(row,text="Radius")
##        label.config(font=('Ariel',10,'bold'))
##        entry = Entry(row)
##
##        label.pack(side='left',padx=5)
##        entry.pack(side='right',padx=5)
##        row.pack()
##        self.entries.append(entry)
##        
##        row = Frame(root)
##        drawButton = Button(row,text="Draw",command=self.draw)
##        drawButton.pack(side='left',padx=5)
##
##        row.pack(padx=5,pady=5)

    def draw(self):
        WIDTH, HEIGHT = 640, 480
        CENTREX, CENTREY = int(WIDTH/2) , int(HEIGHT/2)
        radius = 100

        window = Tk()
        canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
        canvas.pack()
        img = PhotoImage(width=WIDTH, height=HEIGHT)
        canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

        y = 0
        x = radius
        radiusError = 0
        color = "#ffffff"
        while y <= x:
            
            img.put(color, (CENTREX + x,CENTREY + y))
            img.put(color, (CENTREX + y,CENTREY + x))
            img.put(color, (CENTREX - x,CENTREY + y))
            img.put(color, (CENTREX - y,CENTREY + x))
            img.put(color, (CENTREX + x,CENTREY - y))
            img.put(color, (CENTREX + y,CENTREY - x))
            img.put(color, (CENTREX - x,CENTREY - y))
            img.put(color, (CENTREX - y,CENTREY - x))


            if radiusError <= 0:
                y = y + 1
                radiusError = radiusError + 2 * y + 1

            if radiusError > 0:
                x = x - 1
                radiusError = radiusError - 2 * x - 1
        mainloop()
        
            
DC = DrawCircle()
DC.draw()





















