'''
Created on 17/11/2013

@author: rootmaster
'''
from swampy.Gui import *

g = Gui()
g.title('title')
button = g.bu(text='Press me!')
label = g.la(text='Press the button!')

def make_label():
    g.la(text='Thank you!')

button2 = g.bu(text='No, press me!', command=make_label)
    
g.mainloop()