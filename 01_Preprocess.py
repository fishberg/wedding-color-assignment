#!/usr/bin/env python

import pandas as pd
import re

# const lists
RENAME = {
    'Suit or Dress': 'Type',
    'Rank Color Options [Pink [D73B74]]': 'Pink',
    'Rank Color Options [Orange [C14B2D]]': 'Orange',
    'Rank Color Options [Yellow [C28E22]]': 'Yellow',
    'Rank Color Options [Green [105C30]]': 'Green',
    'Rank Color Options [Teal [008293]]': 'Teal',
    'Rank Color Options [Blue [2844AF]]': 'Blue',
    'Rank Color Options [Purple [431174]]': 'Purple',
    'Rank Color Options [Gray [505362]]': 'Gray',
    'Rank Color Options [Brown [7B5933]]': 'Brown',
}

COLORS = [
    'Pink',
    'Orange',
    'Yellow',
    'Green',
    'Teal',
    'Blue',
    'Purple',
    'Gray',
    'Brown',
]

# --------------------------------------

# process DataFrame
df = pd.read_csv('input.csv')  
df.rename(columns=RENAME,inplace=True)
df.drop(columns=['Timestamp','Email Address'],inplace=True)
df.drop_duplicates(subset='Name',keep='last',inplace=True)

# lambda functions
drop_email = lambda x: x.split('<')[0].strip()
drop_choice = lambda x: re.search('\d+',x).group()[0]

# apply lambda functions
df['Name'] = df['Name'].apply(drop_email).astype('string')

for color in COLORS:
    df[color] = df[color].apply(drop_choice).astype(int)

# output `suit.csv` and `dress.csv`
df[df['Type'] == 'Suit'].drop(columns='Type').to_csv('suit.csv',index=False)
df[df['Type'] == 'Dress'].drop(columns='Type').to_csv('dress.csv',index=False)
