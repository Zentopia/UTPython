import pandas as pd
import numpy as np
import gis_demo as gis
import baidu_lbs as bd

df = pd.read_csv('./file/20180107.csv')

with pd.option_context('display.precision', 10):
    print(df)

length = len(df)
result = np.empty((0))

for i in range(0, length - 1, 1):
    dis = (gis.cal_to_coordinate_flat(df['lat'][i], df['lng'][i], df['lat'][i + 1], df['lng'][i + 1]))
    result = np.append(result, dis)

print('间距:', result)
result = result - 1

print('误差:', result)
print('平均误差:', np.average(result), '最大误差:', np.max(result), '最小误差:', np.min(result))

bd_coords = bd.wgs84_to_baidu(df)

print(bd_coords)

bd_length = len(bd_coords)
bd_result = np.empty((0))

for i in range(bd_length - 1):
    p1 = bd_coords[i]
    p2 = bd_coords[i + 1]
    dis = bd.distance(p1.get('lat'), p1.get('lng'), p2.get('lat'), p2.get('lng'))
    bd_result = np.append(bd_result, dis)

print('间距:', bd_result)
bd_result = bd_result - 1

print('误差:', bd_result)
print('平均误差:', np.average(bd_result), '最大误差:', np.max(bd_result), '最小误差:', np.min(bd_result))