'''
Created on 27/10/2013

@author: rootmaster
'''


def printplus20():
    file = open("words.txt", "r")
    for linea in file:
        if len(linea) > 19:
            print(linea)

    file.close()


def verifye(word):
    val = 0
    words = word.lower()
    for letra in words:
        if letra == 'e':
            val += 1

    if val > 0:
        return True

    else:
        return False


def printewords():
    file = open("words.txt", "r")
    cal = 0
    calfile = 0
    for linea in file:
        cal += 1
        if 'e' in linea:
            calfile += 1
            print(linea)

    valor = calfile/cal

    print(cal)
    print(calfile)
    print(valor * 100)
    file.close()

printplus20()

# printewords()
