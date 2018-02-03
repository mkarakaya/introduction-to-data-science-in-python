# -*- coding: utf-8 -*-
import pandas as pd

census_df = pd.read_csv('census.csv', index_col=0, skiprows=1)


def answer_zero():
    return census_df.head()


print answer_zero()
