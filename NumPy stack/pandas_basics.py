# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

## ordinary approach

X = []

for line in open("data_2d.csv"):
    row = line.split(',')
    sample = map(float, row)
    X.append(sample)
    
    
X = np.array(X)    


## pandas

X = pd.read_csv("data_2d.csv")

## convert to matrix(np_array)

M = X.as_matrix()

X[[0,2]]

## lambda

X['x4'] = X.apply(lambda row: row['x1']* row['x2'], axis=1 )


## joins

m = pd.merge(t1, t2, on='user_id')

