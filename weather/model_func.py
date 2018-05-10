# -*- coding: utf-8 -*-

import math
 
# constants
HPA_to_MM = 0.75006168
DSIGN = u'\N{DEGREE SIGN}'
#MSIGN = u'\N{ACUTE ACCENT}'
MSIGN = u'\N{APOSTROPHE}'
#SSIGN = u'\N{DOUBLE ACUTE ACCENT}'
SSIGN = u'\N{QUOTATION MARK}'

side_letter = {0:'С',1:'СВ',2:'В',3:'ЮВ',4:'Ю',5:'ЮЗ',6:'З',7:'СЗ'}
side_arrow ={
    0: u'\N{UPWARDS ARROW}',
    1: u'\N{NORTH EAST ARROW}',
    2: u'\N{RIGHTWARDS ARROW}',
    3: u'\N{SOUTH EAST ARROW}',
    4: u'\N{DOWNWARDS ARROW}',
    5: u'\N{SOUTH WEST ARROW}',
    6: u'\N{LEFTWARDS ARROW}',
    7: u'\N{NORTH WEST ARROW}'
}
def day_duration(sunrise,sunset):
    dura = sunset - sunrise
    hours = dura // (60 * 60)
    minutes = (dura - 3600 * hours) // 60
    seconds = dura - 3600 * hours - 60 * minutes
    return '{H:02d}:{M:02d}'.format(H=hours, M=minutes)

def set_pressure(pressure):
    if pressure:
        return int(pressure * HPA_to_MM)
    else:
        return 'н/д'

def set_wind_direction(deg):
    index = int(((deg + 22.5) % 360) // 45)
    return side_arrow[index] + ' ' + side_letter[index] 
        
def natural_time(timestamp):
    from datetime import datetime as d
    return d.fromtimestamp(timestamp)

def coordinate(val, type):
    ddd = abs(float(val))
    dd = math.trunc(ddd)
    mm = math.trunc((ddd - dd) * 60)
    ss = math.trunc(((ddd - dd) * 60 - mm) * 60)
    if type == 'lon':
        side = 'W' if float(val) < 0 else 'E'
    elif type == 'lat':
        side = 'S' if float(val) < 0 else 'N'
        
    return u'{dd}{dsign}{mm}{msign}{ss}{ssign}{side}'.format(dd=dd, mm=mm, ss=ss, side=side, dsign=DSIGN, msign=MSIGN, ssign=SSIGN)

