# -*- coding: utf-8 -*-
import pandas as pd

census_df = pd.read_csv('census.csv')


def answer_six():
    census_df_filtered = census_df[(census_df['SUMLEV'] == 50)].copy()
    census_df_filtered = census_df_filtered.groupby('STNAME')['POPESTIMATE2015'].nlargest(3)
    #return list(census_df_filtered.groupby('STNAME').sum().nlargest(3).index)
    return census_df_filtered


def answer_five():
    return census_df.groupby('STNAME')['COUNTY'].count().idxmax()


def answer_zero():
    return census_df.head()


print answer_six()
