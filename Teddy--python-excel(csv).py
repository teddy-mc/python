import pandas as pd
import numpy as np
import os
from pandas import DataFrame
import re

df = pd.read_excel(r'C:\EXCEL\0202_201801_i_entryid_python.xls',encoding='ansi')
print(df.head(20))
print(df.dtypes)
df_1 = df.loc[:,'商品编号']
print(df_1.head(20))