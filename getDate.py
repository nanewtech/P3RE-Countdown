import time
import math

release = 1706860800000

def getDaysExact() -> str:
    unix = time.time() * 1000
    diff = release - unix

    #calc days until then remove from calc
    days = math.floor(diff / 86400000)
    diff = diff - days * 86400000

    # calc hours until then remove from calc
    hours = math.floor(diff / 3600000)
    diff = diff - hours * 3600000

    minutes = math.floor(diff / 60000)
    diff = diff - minutes * 60000

    seconds = math.floor(diff / 1000)
    diff = diff - seconds * 1000

    milliseconds = diff

    return f'{days} days, {hours} hours, {minutes} minutes, {seconds} seconds and {milliseconds} milliseconds'


def getWeeksDays() -> str:

    unix = time.time() * 1000
    diff = release - unix

    #get ammount of weeks left, only real numbers -> remove weeks already counted from time left
    weeks = math.floor(diff / 604800000)
    diff = diff - weeks * 604800000
    #get days, only real numbers
    days = math.floor(diff / 86400000)
    if days >= 2:
        return f'{weeks} weeks and {days} days'
    elif days == 1:
        return f'{weeks} weeks and {days} day'
    else: return f'{weeks} weeks'

def getDays() -> str:
    unix = time.time() * 1000
    diff = release - unix

    days = math.floor(diff / 86400000)
    diff = diff - days * 86400000
    return f'{days} days'
