'''
Created on 22/11/2013

@author: rootmaster
'''
from swampy.Gui import *

g = Gui()
g.title("")
canvas = g.ca(width=500, height=500)
label = g.la(text="Press the Button!")

def drawCircle():
    item = canvas.circle([0,0], 100, fill='red')

button = g.bu(text="Activate Me!", command=drawCircle)
    
g.mainloop()