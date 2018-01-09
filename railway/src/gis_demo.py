#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.ticker as tik
import numpy as np
import math

EARTH_RADIUS = 6378137.0

def _get_pad(d):
	return d*math.pi/180.0


def _cal_to_coordinate(lat1,lng1,lat2,lng2):

    """
    北斗坐标计算距离
    """
    radLat1 = _get_pad(lat1)
    radLat2 = _get_pad(lat2)
        
    a = radLat1 - radLat2
    b = _get_pad(lng1) - _get_pad(lng2)
        
    s = 2*math.asin(math.sqrt(math.pow(math.sin(a/2),2) + math.cos(radLat1)*math.cos(radLat2)*math.pow(math.sin(b/2),2)))
    s = s*EARTH_RADIUS
    s = round(s*10000)/10000.0
                
    return s


def cal_to_coordinate_flat(lat1,lng1,lat2,lng2):
    """
    北斗坐标计算距离(椭圆)
    """
    f = _get_pad((lat1 + lat2)/2)
    g = _get_pad((lat1 - lat2)/2)
    l = _get_pad((lng1 - lng2)/2)
        
    sg = math.sin(g)
    sl = math.sin(l)
    sf = math.sin(f)
        

    a = EARTH_RADIUS
    fl = 1/298.257;
        
    sg = sg*sg
    sl = sl*sl
    sf = sf*sf
        
    s = sg*(1-sl) + (1-sf)*sl
    c = (1-sg)*(1-sl) + sf*sl
        
    w = math.atan(math.sqrt(s/c))
    r = math.sqrt(s*c)/w
    d = 2*w*a
    h1 = (3*r -1)/2/c
    h2 = (3*r +1)/2/s
        
    return round(d*(1 + fl*(h1*sf*(1-sg) - h2*(1-sf)*sg)), 5)


def test():
    print('Su')

if __name__ == '__main__':

	# lat1 = 40.07834518833333  	#百度坐标：40.08551585036245
	# lng1 = 116.35229350833333   #百度坐标：116.3650760781415


	# lat2 = 40.078343548333336   #百度坐标：40.08551432847522
	# lng2 = 116.35230061166666	#百度坐标：116.3650830928695

    """
    采用百度接口进行测距：0.62253m
    """

    #print(_cal_to_coordinate(lat1,lng1,lat2,lng2))

    #print(_cal_to_coordinate_flat(lat1,lng1,lat2,lng2)) #0.63266


    """
    采用百度接口进行测距：28.66m
    """

    # lat3 = 40.06148084833333    #百度坐标：40.068496292867
    # lng3 = 116.34078560166667   #百度坐标：116.35357120258114


    # lat4 = 40.06173812833333    #百度坐标：40.06875366929153
    # lng4 = 116.34076853166667	#百度坐标：116.35355431178137

    #print(_cal_to_coordinate_flat(lat3,lng3,lat4,lng4)) #28.60446


    lat3 = 40.049255738333336

    lng3 = 116.34384970166667


    lat4 = 40.049269198333334    
    lng4 = 116.343844065   

    print(cal_to_coordinate_flat(lat3,lng3,lat4,lng4))
