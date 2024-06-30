#!/usr/bin/env python

import pandas as pd
import random

# select which file to load
df = pd.read_csv('suit.csv')
#df = pd.read_csv('dress.csv')

# --------------------------------------

df.set_index('Name',inplace=True)

for rank in range(1,len(df.columns)+1):
    for color in df:
        voters = list(df[df[color] == rank].index)
        if len(voters) > 0:
            selected = random.sample(voters,1)[0]
            df.drop(index=selected,inplace=True)
            df.drop(columns=color,inplace=True)
            print(f'{selected} -> {color}')
