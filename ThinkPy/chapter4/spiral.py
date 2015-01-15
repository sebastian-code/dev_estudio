'''
Created on 14/10/2013
@summary: Aplicacion creada a manera de ejercicio para afianzar conocimientos.
@author: Sebastian Reyes Espinosa.
@version: v1
'''
from swampy.TurtleWorld import *
from TurtleWorld import *

def draw_spiral(t, n, length=3, a=0.1, b=0.0002):
    """Draws an Archimedian spiral starting at the origin.

    Args:
      n: how many line segments to draw
      length: how long each segment is
      a: how loose the initial spiral starts out (larger is looser)
      b: how loosly coiled the spiral is (larger is looser)

    http://en.wikipedia.org/wiki/Spiral
    """
    theta = 0.0

    for i in range(n):
        fd(t, length)
        dtheta = 1 / (a + b * theta)

        lt(t, dtheta)
        theta += dtheta


# create the world and bob
world = TurtleWorld()
bob = Turtle()
bob.delay = 0
draw_spiral(bob, n=1000)

wait_for_user()