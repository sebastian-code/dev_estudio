'''
Created on 15/11/2013

@author: rootmaster
'''

from datetime import datetime

class Time(object):
    """
    Clase concebida para representar el concepto de tiempo en su forma horaria.
    @return: Un objeto del tipo Time() con los siguientes parametros.
    @param hour: Parametro de hora para un objeto Time()
    @param minute: Parametro de minuto para un objeto Time()
    @param second: Parametro de segundo para un objeto Time()
    """
#Varios objetos de la clase Time().

fTime = Time()
fTime.hour = 9
fTime.minute = 59
fTime.second = 30

sTime = Time()
sTime.hour = 10
sTime.minute = 45
sTime.second = 36

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

def printTime(t):
    '''
    @requires: Un objeto del tipo Time()
    @return: Imprime un objeto del tipo Time()
    '''
    print '%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second)

def transTime(t):
    '''
    @requires: Un objeto del tipo Time()
    @return: Un valor en segundos equivalentes al objeto del tipo Time()
    '''
    tf = (t.hour * 60) + t.minute
    tf = (tf * 60) + t.second
    return tf

def isAfter(t1, t2):
    if transTime(t1) < transTime(t2):
        return True
    else:
        return False

def is_after(t1, t2):
    """Returns True if t1 is after t2; false otherwise."""
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

def add_time1(t1, t2):
    summ = Time()
    summ.hour = t1.hour + t2.hour
    summ.minute = t1.minute + t2.minute
    summ.second = t1.second + t2.second
    return summ

def add_time(t1, t2):
    summ = Time()
    summ.hour = t1.hour + t2.hour
    summ.minute = t1.minute + t2.minute
    summ.second = t1.second + t2.second

    if summ.second >= 60:
        summ.second -= 60
        summ.minute += 1
    if summ.minute >= 60:
        summ.minute -= 60
        summ.hour += 1
        
    return summ

def int_to_time(seconds):
    """
    Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def time_to_int(time):
    """Computes the number of seconds since midnight.

    time: Time object.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def add_times(t1, t2):
    """Adds two time objects."""
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def valid_time(time):
    """Checks whether a Time object satisfies the invariants."""
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def increment(t1, seconds):
    """Adds seconds to a Time object."""
    assert valid_time(t1)
    seconds += time_to_int(t1)
    return int_to_time(seconds)


def mul_time(t1, factor):
    """Multiplies a Time object by a factor."""
    assert valid_time(t1)
    seconds = time_to_int(t1) * factor
    return int_to_time(seconds)


def days_until_birthday(birthday):
    """How long until my next birthday?"""
    today = datetime.today()
    # when is my birthday this year?
    next_birthday = datetime(today.year, birthday.month, birthday.day)

    # if it has gone by, when will it be next year
    if today > next_birthday:
        next_birthday = datetime(today.year+1, birthday.month, birthday.day)

    # subtraction on datetime objects returns a timedelta object
    delta = next_birthday - today
    return delta.days


def double_day(b1, b2):
    """Compute the day when one person is twice as old as the other.

    b1: datetime birthday of the younger person
    b2: datetime birthday of the older person
    """
    assert b1 > b2
    delta = b1 - b2
    double_day = b1 + delta
    return double_day


def datetime_exercises():
    # print today's day of the week
    today = datetime.today()
    print today.weekday()
    print today.strftime('%A')

    # compute the number of days until the next birthday
    # (note that it usually gets rounded down)
    birthday = datetime(1967, 5, 2)
    print 'Days until birthday',
    print days_until_birthday(birthday)

    # compute the day one person is twice as old as another
    b1 = datetime(2006, 12, 26)
    b2 = datetime(2003, 10, 11)
    print 'Double Day',
    print double_day(b1, b2)
    
done = add_time(start, duration)
printTime(done)

#printTime(fTime)

#print is_after(fTime, sTime)

