# -*- coding: utf-8 -*-

import math
from django.utils.encoding import smart_text

# Constants
HPA_to_MM = 0.75006168
DSIGN = u'\N{DEGREE SIGN}'
MSIGN = u'\N{APOSTROPHE}'
SSIGN = u'\N{QUOTATION MARK}'

TEMP_MIN = u'\N{DOWNWARDS ARROW TO BAR}'
TEMP_MAX = u'\N{UPWARDS ARROW TO BAR}'

side_letter = {
    0: u'С',
    1: u'СВ',
    2: u'В',
    3: u'ЮВ',
    4: u'Ю',
    5: u'ЮЗ',
    6: u'З',
    7: u'СЗ'
    }

side_arrow = {
    0: u'\N{UPWARDS ARROW}',
    1: u'\N{NORTH EAST ARROW}',
    2: u'\N{RIGHTWARDS ARROW}',
    3: u'\N{SOUTH EAST ARROW}',
    4: u'\N{DOWNWARDS ARROW}',
    5: u'\N{SOUTH WEST ARROW}',
    6: u'\N{LEFTWARDS ARROW}',
    7: u'\N{NORTH WEST ARROW}'
    }

conditions = {
    200: u'гроза с небольшим дождем',
    201: u'гроза с дождем',
    202: u'гроза с сильным дождем',
    210: u'легкая гроза',
    211: u'гроза',
    212: u'сильная гроза',
    221: u'шквальная гроза',
    230: u'гроза с легкой моросью',
    231: u'гроза с дождем',
    232: u'гроза с проливным дождем',
    300: u'малая изморось',
    301: u'изморось',
    302: u'сильный дождь',
    310: u'легкий дождь, изморось',
    311: u'дождь, изморось',
    312: u'сильный дождь, изморось',
    313: u'ливень и изморось',
    314: u'сильный ливень и изморось',
    321: u'ливневый дождь',
    500: u'легкий дождь',
    501: u'умеренный дождь',
    502: u'интенсивный дождь',
    503: u'очень сильный дождь',
    504: u'сильный дождь',
    511: u'ледяной дождь',
    520: u'легкий ливень',
    521: u'ливень',
    522: u'сильный ливень',
    531: u'шквальный ливневый дождь',
    600: u'легкий снег',
    601: u'снег',
    602: u'снегопад',
    611: u'дождь со снегом',
    612: u'дождь',
    615: u'легкий дождь и снег',
    616: u'дождь и снег',
    620: u'легкий душ снег',
    621: u'снегопад',
    622: u'сильный снегопад',
    701: u'туман',
    711: u'дым',
    721: u'мгла',
    731: u'песок, пылевые завихрения',
    741: u'туман',
    751: u'песок',
    761: u'пыль',
    762: u'вулканический пепел',
    771: u'шквалы',
    781: u'торнадо',
    800: u'чистое небо',
    801: u'малоблачно',
    802: u'рассеянные облака',
    803: u'рваные облака',
    804: u'облака с просветом',
    900: u'торнадо',
    901: u'тропическая буря',
    902: u'ураган',
    903: u'холод',
    904: u'жара',
    905: u'ветрено',
    906: u'град',
    951: u'спокойный',
    952: u'легкий ветерок',
    953: u'нежный бриз',
    954: u'умеренный ветерок',
    955: u'свежий ветерок',
    956: u'сильный ветер',
    957: u'сильный ветер, почти шторм',
    958: u'шторм',
    959: u'сильный шторм',
    960: u'буря',
    961: u'сильный шторм',
    962: u'ураган'
    }


def day_duration(sunrise, sunset):
    dura = sunset - sunrise
    hours = dura // (60 * 60)
    minutes = (dura - 3600 * hours) // 60
    # seconds = dura - 3600 * hours - 60 * minutes
    return '{H:02d}:{M:02d}'.format(H=hours, M=minutes)


def set_condition(condition, description):
    res = ''
    if condition:
        res = conditions[condition]
    if res != description:
        res += ', ' + description
    return smart_text(res)


def set_pressure(pressure):
    return int(pressure * HPA_to_MM) if pressure else 'н/д'


def set_wind_direction(deg):
    if deg is None:
        return ''
    else:
        index = int(((deg + 22.5) % 360) // 45)
        return smart_text(side_arrow[index] + ' ' + side_letter[index])


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

    return u'{side} {dd}{dsign}{mm}{msign}{ss}{ssign}'.format(
        dd=dd,
        mm=mm,
        ss=ss,
        side=side,
        dsign=DSIGN,
        msign=MSIGN,
        ssign=SSIGN
        )

def min_max_temperature(min, max):
    return u'{min_sign}{min} {max_sign}{max}'.format(
        min_sign=TEMP_MIN,
        min=min,
        max_sign=TEMP_MAX,
        max=max,
        )
    