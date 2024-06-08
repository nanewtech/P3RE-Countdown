import time
import math

release = 1725926400000

def getDaysExact():
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
    if days == 0:
        if hours == 0:
            if minutes == 0:
                if seconds == 0: 
                    return 0
                else:
                    return f'{seconds} seconds and {milliseconds} milliseconds'
            else:
                return f'{minutes} minutes, {seconds} seconds and {milliseconds} milliseconds'
        else:
            return f'{hours} hours, {minutes} minutes, {seconds} seconds and {milliseconds} milliseconds'
    
    else:
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
        if weeks >= 1:
            return f'{weeks} week and {days} days'
        else:
            return f'{days} days'
    elif days == 1:
        if weeks >= 1:
            return f'{weeks} week and {days} day'
        else:
            return f'{days} day'
    else: 
        if not weeks == 0:
            return f'{weeks} week'
        else:
            return 0
    

def getDays() -> str:
    unix = time.time() * 1000
    diff = release - unix

    days = math.floor(diff / 86400000)
    diff = diff - days * 86400000
    return f'{days} days'
