'''
Created on 11/11/2013

@author: rootmaster
'''
# the following example “walks” through a directory, prints
# the names of all the files, and calls itself recursively on all the directories.

import os

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

    if os.path.isfile(path):
        print path

    else:
        walk(path)

def sed(pattern, replace, source, dest):
    try:
        fIn = open(source, 'r')
        fOut = open(dest, 'w')
        for topic in fIn:
            topic = topic.replace(pattern, replace)
            fOut.write(topic)
        
        fIn.close()
        fOut.close()
    
    except:
        print 'Carajo, la mondamos!'

    
    