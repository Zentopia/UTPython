import requests
import json
import numpy as np
import math
import sys
import pandas as pd

def wgs84_to_baidu(df):

    length = len(df)

    coords = ''
    for i in range(length):
        if len(coords) > 0:
            coords = coords + ';'
        lat = df['lat'][i]
        lng = df['lng'][i]
        coord = str(lng) + ',' + str(lat)
        coords = coords + coord

    ak = 'epNGxPlcmr3LTHiRimFSFzBgSaFgokHc'
    URL = 'http://api.map.baidu.com/geoconv/v1/'
    from_ = 1
    to = 5
    PARAMS = {
                'coords': coords,
                'from': from_,
                'to': to,
                'ak': ak
              }
    headers = {'content-type': 'application/json'}
    request = requests.get(url=URL, params=PARAMS, headers = headers)
    json_content = request.content
    content = json.loads(json_content)
    status = content.get('status')
    print('status:', status)
    if status != 0:
        return

    result = content.get('result')
    result_np = np.empty((0))
    for dic in result:
        lng = dic.get('x')
        lat = dic.get('y')
        coord = [lng, lat]
        new_dic = {
            'lng' : lng,
            'lat' : lat
        }
        result_np = np.append(result_np, new_dic)

    print(result_np)

    return result_np

def P(x):
    return math.pi/180*x

def distance(lng1, lat1, lng2, lat2):
    return 6370996.81 * math.acos(math.sin(P(lat1)) * math.sin(P(lat2)) + math.cos(P(lat1)) * math.cos(P(lat2)) * math.cos(P(lng2) - P(lng1)))






