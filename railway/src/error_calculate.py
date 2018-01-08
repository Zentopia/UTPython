import pandas as pd
import numpy as np
import gis_demo as gis

df = pd.read_csv('20180107_new.csv')

with pd.option_context('display.precision', 10):
    print(df)

length = len(df)
result = np.empty((0))

for i in range(0, length - 1, 1):
    print(i)
    dis = (gis.cal_to_coordinate_flat(df['lat'][i], df['lng'][i], df['lat'][i + 1], df['lng'][i + 1]))
    result = np.append(result, dis)

print('间距:', result)
result = result - 1

print('误差:', result)
print('平均误差:', np.average(result), '最大误差:', np.max(result), '最小误差:', np.min(result))
