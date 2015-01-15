'''
Created on 17/11/2013

@author: rootmaster
'''
class Kangaroo():
    def __init__(self, contents = []):
        self.pouch_contents = contents
    
    def put_in_pouch(self, obj):
        self.pouch_contents.append(obj)
    
    def __str__(self):
        t = [ object.__str__(self) + ' with pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)