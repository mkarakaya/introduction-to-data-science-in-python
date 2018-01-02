# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)


for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[0].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')


def answer_one():
    return df[df['Gold'] == df['Gold'].max()].index[0]


def answer_zero():
    return df.iloc[0]


print answer_one()
