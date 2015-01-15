'''
Created on 15/11/2013

@author: rootmaster
'''

from swampy.World import World

world = World()
canv = world.ca(500, 500, background='white')
rect = [[-150, -150], [150, 150]]

def draw_rectangle(canvas, rectang, clr):
    canvas.rectangle(rectang, fill= clr)
    world.mainloop()

draw_rectangle(canv, rect, 'blue')
