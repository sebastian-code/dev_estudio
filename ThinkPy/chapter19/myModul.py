'''
Created on 17/11/2013
@author: rootmaster
'''

from swampy.Gui import *

g = Gui()
g.title('')

def callback1():
    g.bu(text='Now press me.', command=callback2)

def callback2():
    g.la(text='Nice job.')

def make_label():
    g.la(text='Thank you.')

button2 = g.bu(text='No, press me!', command=make_label)
g.bu(text='Press me.', command=callback1)


g.mainloop()