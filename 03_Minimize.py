#!/usr/bin/env python

import subprocess
import re
from tqdm.auto import tqdm

def get_cost(filepath):
    res = subprocess.check_output(['./02_Assign.py',filepath]).decode('utf-8')
    ranks = list(map(int,re.findall('\((.*)\)',res)))
    cost = sum(ranks)
    return cost,res

def run_sim(filepath,NUM_ITER=100):
    D = {}

    for i in tqdm(range(NUM_ITER)):
        cost,res = get_cost(filepath)
        if not cost in D:
            D[cost] = set([])
        D[cost].add(res)

    min_cost = min(D)
    print(f'min_cost = {min_cost}')
    for s in D[min_cost]:
        print(s)

run_sim('suit.csv')
run_sim('dress.csv')
