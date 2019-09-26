import pandas as pd
import numpy as np
from pydataset import data

mpg = data('mpg')
mpg.head(2)

#1.a
mpg.head(2)
mpg['total_mpg'] = (mpg['cty'] + mpg['hwy'])/2
mpg.head(2)
mpg.groupby('manufacturer').total_mpg.agg('mean').sort_values(ascending = False).head(1)

#1.b
len(mpg[['manufacturer']].groupby('manufacturer').agg('count'))

#1.c

len(mpg[['model']].groupby('model').agg('count'))


#1.d
mpg['automatic_trans'] = mpg['trans'].str.contains('auto')
mpg.head(3)

mpg[['automatic_trans','model']].groupby('automatic_trans').agg('count')